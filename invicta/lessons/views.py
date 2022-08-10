from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse
from lessons.models import Lesson, Program
from urls import reverse_lazy

# Create your views here.

class CreateProgram(LoginRequiredMixin, generic.CreateView):
    model = Program
    fields = ("day", "time")
    template_name = "lessons/program_form.html"

    def form_valid(self, form):
        form.instance.teacher = self.request.user.teacher
        return super(CreateProgram, self).form_valid(form)

class ListPrograms(LoginRequiredMixin, generic.ListView):
    model = Program
    select_related = ('user')

    def get_success_url(self):
        return reverse_lazy('home', kwargs={'uname': self.request.user.username })
