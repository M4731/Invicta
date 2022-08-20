from django.shortcuts import render
from reviews.models import Review
from accounts.models import User, Teacher
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.db import IntegrityError
import logging
from invicta.decorators import student_required, teacher_required
from django.urls import reverse_lazy, reverse
from django.contrib import messages

class CreateReview(LoginRequiredMixin, generic.CreateView):
    fields = ("rating", "description")
    model = Review
    template_name = 'reviews/review_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.teacher = Teacher.objects.get(pk=self.kwargs.get('pk'))

        # if len(Review.objects.all(user=self.request.user, teacher=Teacher.objects.get(pk=self.kwargs.get('pk')))) != 0:
        #     return reverse('reviews:student_reviews', kwargs=self.request.user.pk)
        return super(CreateReview, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_object'] = Teacher.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy("reviews:student_reviews", kwargs={'pk': self.request.user.pk})

class StudentReviews(generic.ListView):
    model = Review
    template_name = 'reviews/student_reviews_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(StudentReviews, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class DeleteReview(LoginRequiredMixin, generic.DeleteView):
    model = Review
    template_name = "reviews/review_confirm_delete.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)
    
    def get_success_url(self, **kwargs):
        return reverse_lazy("reviews:student_reviews", kwargs={'pk': self.request.user.pk})

class UpdateReview(LoginRequiredMixin,generic.UpdateView):
    fields = ["rating","description"]
    model = Review
    template_name = 'reviews/review_update.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy("reviews:student_reviews", kwargs={'pk': self.request.user.pk})

class TeacherReviews(generic.ListView):
    model = Review
    template_name = 'reviews/teacher_reviews_list.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super(TeacherReviews, self).get_queryset()
        queryset = queryset.filter(teacher=self.request.user.teacher)
        return queryset

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher'] = self.request.user.teacher
        return context