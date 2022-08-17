from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from lessons.models import Lesson
from accounts.models import Teacher
from django.http.response import HttpResponseRedirect
import datetime

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

        return HttpResponseRedirect(request.path)