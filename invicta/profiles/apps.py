from django.apps import AppConfig
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


# class ProfilesConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'profiles'

class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
    verbose_name = _('profiles')

    def ready(self):
        import profiles.signals  # noqa
