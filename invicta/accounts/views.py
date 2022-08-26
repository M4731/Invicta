from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from accounts.models import User, Teacher
from accounts.forms import StudentSignUpForm, TeacherSignUpForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from invicta.decorators import student_required, teacher_required

class StudentSignUpView(CreateView):
    form_class = StudentSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class TeacherSignUpView(CreateView):
    form_class = TeacherSignUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

@method_decorator([login_required], name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['username','first_name','last_name','email','phone_number']
    template_name = 'accounts/update.html'

    def get_success_url(self):
        return reverse('home')
    
    def form_valid(self, form):
        self.object = form.save()
        return super(UserUpdateView,self).form_valid(form)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.user.id
        return context

@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherUpdateView(UpdateView):
    model = User
    fields = ['username','first_name','last_name','email','phone_number']
    template_name = 'accounts/update_teacher.html'

    def get_success_url(self):
        return reverse('home')
    
    def form_valid(self, form):
        self.object = form.save()
        return super(TeacherUpdateView,self).form_valid(form)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['user_id'] = self.request.user.pk
        return context

@method_decorator([login_required, teacher_required], name='dispatch')
class TeacherInfoUpdateView(UpdateView):
    model = Teacher
    fields = ['price','subject']
    template_name = 'accounts/update_teacher_info.html'

    def get_success_url(self):
        return reverse('home')
    
    def form_valid(self, form):
        self.object = form.save()
        return super(TeacherInfoUpdateView,self).form_valid(form)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_id'] = self.request.user.teacher.pk
        return context