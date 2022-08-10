from django.db import models
from accounts.models import Teacher, User 
from datetime import timedelta
from django.urls import reverse

class Program(models.Model):
    possible_hours = (
        ('8-10', '08:00-10:00'),
        ('10-12', '10:00-12:00'),
        ('12-14', '12:00-14:00'),
        ('14-16', '14:00-16:00'),
        ('16-18', '16:00-18:00'),
        ('18-20', '18:00-20:00'),
        ('20-22', '20:00-22:00'),
    )

    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day = models.DateField()
    time = models.CharField(max_length=5,choices = possible_hours)

    class Meta:
        unique_together = ['teacher', 'day','time']
        ordering = ['day','time']

    def __str__(self):
        return self.teacher.user.first_name + " " + self.teacher.user.last_name + " " + str(self.day) + " " + self.time
    
    def get_absolute_url(self):
        return reverse('home')

class Lesson(models.Model):
    title = models.CharField(max_length=264, default="Basic Lesson")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE) #, editable=False, default='', blank=True
    program = models.OneToOneField(Program, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    # def save(self,*args, **kwargs):
    #     super().save(*args, **kwargs)

