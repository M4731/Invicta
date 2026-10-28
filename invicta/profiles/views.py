from django.shortcuts import render
from django.contrib.auth.decorators import login_required 
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from profiles.models import Profile
from django.urls import reverse_lazy, reverse
from accounts.models import Teacher
from lessons.models import Lesson
from reviews.models import Review
from invicta.decorators import student_required, teacher_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator([login_required], name='dispatch')
class ProfileDetail(LoginRequiredMixin, generic.DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_student:
            context['existing_review'] = Review.objects.filter(
                user=self.request.user, teacher=self.object.teacher
            ).first()
            context['can_review'] = Lesson.objects.filter(
                user=self.request.user, teacher=self.object.teacher, accepted=True
            ).exists()
        return context

@method_decorator([login_required, teacher_required], name='dispatch')
class ProfileUpdate(LoginRequiredMixin, generic.edit.UpdateView):
    model = Profile
    fields = ['avatar','description']
    template_name = 'profiles/profile_update.html'

    def get_queryset(self):
        return super().get_queryset().filter(teacher__user=self.request.user)

    def get_success_url(self):
        return reverse('profiles:profile_detail', kwargs={'slug': self.object.slug})
    
    def form_valid(self, form):
        self.object = form.save()
        return super(ProfileUpdate,self).form_valid(form)
