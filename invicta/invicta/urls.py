from django.contrib import admin
from django.urls import path, include
from invicta import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(), name='home'),
    path('test/',views.TestPage.as_view(), name='test'),
    path('thanks/',views.ThanksPage.as_view(), name='thanks'),
    path('accounts/',include('accounts.urls', namespace='accounts')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('lessons/',include('lessons.urls', namespace='lessons')),
]
