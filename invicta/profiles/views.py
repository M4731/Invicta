from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from profiles.models import Profile
from django.urls import reverse_lazy, reverse

class ProfileDetail(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

class ProfileUpdate(LoginRequiredMixin, generic.edit.UpdateView):
    model = Profile
    fields = ['avatar','description']
    template_name = 'profiles/profile_update.html'

    def get_success_url(self):
        if self.object.avatar:
            return reverse('profiles:profile_detail', kwargs={'slug': self.object.slug})
        else:
            return reverse('home')
    
    def form_valid(self, form):
        self.object = form.save()
        return super(ProfileUpdate,self).form_valid(form)

    