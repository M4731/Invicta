from django.db import models
from django.utils.text import slugify
from accounts.models import User, Teacher
from django.urls import reverse

class Profile(models.Model):
    teacher = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    slug = models.SlugField(allow_unicode=True,unique=True, null=True, blank=True)

    def __str__(self):
        return self.teacher.username

    def save(self,*args, **kwargs):
        self.slug = slugify(self.teacher.username)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profiles:profile_details',kwargs={'slug':self.slug})