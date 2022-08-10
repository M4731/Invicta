from django.contrib import admin
from profiles.models import Profile
from django.apps import AppConfig

admin.site.register(Profile)

class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals