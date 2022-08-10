from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from profiles.models import Profile

class ProfileDetail(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'