from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from lessons.models import Lesson
from accounts.models import Teacher
from django.http.response import HttpResponseRedirect
import datetime
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage, message, send_mail
from django.conf import settings
import smtplib
import logging

class CreateLesson(LoginRequiredMixin, generic.CreateView):
    fields = ("description", "time_description")
    model = Lesson
    template_name = 'lessons/lesson_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.teacher = Teacher.objects.get(pk=self.kwargs.get('pk'))
        return super(CreateLesson, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_id'] = Teacher.objects.get(pk=self.kwargs.get('pk')).pk
        return context

class TeacherLessons(generic.ListView):
    model = Lesson
    template_name = 'lessons/teacher_lessons_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(TeacherLessons, self).get_queryset()
        queryset = queryset.filter(teacher=self.request.user.teacher)
        return queryset

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = self.request.user.teacher
        return context

    def post(self, request, pk):
        date = request.POST.get("date")
        time = request.POST.get("time")
        lesson_id = request.POST.get("lesson_id")
        
        lesson_object = Lesson.objects.get(id=lesson_id)
        lesson_object.accepted = True
        lesson_object.planned_date = date
        lesson_object.planned_time = time
        lesson_object.save()

        data = {
            "student_fname":lesson_object.user.first_name,
            "student_lname":lesson_object.user.last_name,
            "teacher_fname":lesson_object.teacher.user.first_name,
            "teacher_lname":lesson_object.teacher.user.last_name,
            "date":lesson_object.planned_date,
            "time":lesson_object.planned_time,
        }

        message = get_template('lessons/lesson_confirmation_email.html').render(data)
        title = "Lesson Approvement (DO NOT REPLY)"
        send_mail(title, message, settings.EMAIL_HOST_USER, [lesson_object.user.email])

        # # try:
        # server = smtplib.SMTP("smtp.gmail.com", 587)
        # server.ehlo()
        # server.starttls()
        # server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        # server.sendmail(settings.EMAIL_HOST_USER, [lesson_object.user.email], message)
        # server.close()
        # logging.info('successfully sent the mail')
        # # except:
        # #     logging.error("failed to send mail") 

        messages.add_message(request, messages.SUCCESS, f"You accepted the appointment of {lesson_object.user.first_name} {lesson_object.user.last_name}")

        return HttpResponseRedirect(request.path)

class StudentLessons(generic.ListView):
    model = Lesson
    template_name = 'lessons/student_lessons_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(StudentLessons, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context