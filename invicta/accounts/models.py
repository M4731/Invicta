from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def phone_number_validator(value):
    if len(value) != 10:
        raise ValidationError(
            _('%(value)s is not a valid phone number.'),
            params={'value': value},
        )
    for x in value:
        if x > '9' or x < '0':
            raise ValidationError(
                _('%(value)s is not a valid phone number.'),
                params={'value': value},
            ) 
    if value[0] != '0':
        raise ValidationError(
            _('%(value)s is not a valid phone number.'),
            params={'value': value},
        )

class Subject(models.Model):
    name = models.CharField(max_length=264)

    def __str__(self):
        return self.name

class User(AbstractUser):
    phone_number = models.CharField(max_length=10,blank=False, validators=[phone_number_validator], unique=True)
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + str(self.is_teacher)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(default=100)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_teacher_rating(self):
        x = 0
        i = 0
        reviews = self.review_set.all()
        if len(reviews) != 0:
            for review in reviews:
                x += review.rating
                i += 1
            return x/i
        else: 
            return 0
 