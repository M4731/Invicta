from django.shortcuts import render
from reviews.models import Review
from accounts.models import User, Teacher
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

class CreateReview(LoginRequiredMixin, generic.CreateView):
    fields = ("rating", "description")
    model = Review
    template_name = 'reviews/review_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.teacher = Teacher.objects.get(pk=self.kwargs.get('pk'))
        return super(CreateReview, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_object'] = Teacher.objects.get(pk=self.kwargs.get('pk'))
        return context
