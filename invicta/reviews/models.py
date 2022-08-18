from django.db import models
from accounts.models import User, Teacher
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import IntegrityError
import logging

def rating_validator(value):
    if value > 10 or value < 1:
        raise ValidationError(
            _('The rating can not be less than 1 and higher than 10.'),
            params={'value': value},
        )

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    sent_date = models.DateField(auto_now_add=True)
    description = models.TextField()
    rating = models.PositiveIntegerField(validators = [rating_validator])

    def __str__(self):
        return self.user.username + self.teacher.user.username 
    
    class Meta:
        ordering = ["-sent_date"]
        unique_together = ['user', 'teacher']

    def get_absolute_url(self):
        return reverse('home')

    def save(self, *args, **kwargs):
        try:
            # self.name = 'kevin'
            super(Review, self).save(*args, **kwargs)
        except IntegrityError:
            logging.error("You already left a review for this teacher!")