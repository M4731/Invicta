from django.db import models
from accounts.models import User, Teacher
from django.urls import reverse

class Lesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    planned_date = models.DateField(auto_now_add=False, null=True, blank=True)
    description = models.TextField()
    time_description = models.TextField(default="Sunt liber oricand.")

    def __str__(self):
        return self.user.username + self.teacher.user.username 
    
    class Meta:
        ordering = ["-sent_date"]

    def get_absolute_url(self):
        return reverse('home')