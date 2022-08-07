from django.contrib.auth.models import AbstractUser
from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=264)

    def __str__(self):
        return self.name

class User(AbstractUser):
    phone_number = models.CharField(max_length=10,blank=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ---TEACHER:' + str(self.is_teacher)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
