from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.views import generic
from lessons.models import Lesson
from django.shortcuts import get_object_or_404
from accounts.models import Teacher

class CreateLesson(LoginRequiredMixin, generic.CreateView):
    fields = ("description", "time_description")
    model = Lesson
    template_name = 'lessons/lesson_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.teacher = Teacher.objects.get(pk=self.kwargs.get('pk'))
        return super(CreateLesson, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['teacher_id'] = Teacher.objects.get(pk=self.kwargs.get('pk')).pk
        return context