from django.contrib import admin
from accounts.models import Subject, Teacher, User

# Register your models here.
admin.site.register(Subject)
admin.site.register(User)
admin.site.register(Teacher)
