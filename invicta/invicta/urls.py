from django.contrib import admin
from django.urls import path, include
from invicta import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(), name='home'),
    path('test/',views.TestPage.as_view(), name='test'),
    path('thanks/',views.ThanksPage.as_view(), name='thanks'),
    path('accounts/',include('accounts.urls', namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('profiles/',include('profiles.urls', namespace='profiles')),
    path('teachers',views.ListTeachers.as_view(),name="all_teachers"),
    path('lessons/',include('lessons.urls', namespace='lessons')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
