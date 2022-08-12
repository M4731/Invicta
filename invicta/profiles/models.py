from django.db import models
from django.utils.text import slugify
from accounts.models import User, Teacher
from django.urls import reverse

class Profile(models.Model):
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    avatar = models.ImageField(default='profile_images/default.jpg', upload_to='profile_images')
    description = models.TextField(default="Not yet edited description")
    slug = models.SlugField(allow_unicode=True,unique=True, null=True, blank=True)

    def __str__(self):
        return self.teacher.user.username

    def save(self,*args, **kwargs):
        self.slug = slugify(self.teacher.user.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profiles:profile_details',kwargs={'slug':self.slug})