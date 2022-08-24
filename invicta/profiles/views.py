from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from profiles.models import Profile
from django.urls import reverse_lazy, reverse
from accounts.models import Teacher
from invicta.decorators import student_required, teacher_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator([login_required], name='dispatch')
class ProfileDetail(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

@method_decorator([login_required, teacher_required], name='dispatch')
class ProfileUpdate(LoginRequiredMixin, generic.edit.UpdateView):
    model = Profile
    fields = ['avatar','description']
    template_name = 'profiles/profile_update.html'

    def get_success_url(self):
        return reverse('profiles:profile_detail', kwargs={'slug': self.object.slug})
    
    def form_valid(self, form):
        self.object = form.save()
        return super(ProfileUpdate,self).form_valid(form)

    