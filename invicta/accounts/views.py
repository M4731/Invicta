from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from accounts.models import User
from accounts.forms import StudentSignUpForm, TeacherSignUpForm
from django.urls import reverse_lazy

class StudentSignUpView(CreateView):
    form_class = StudentSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class TeacherSignUpView(CreateView):
    form_class = TeacherSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'