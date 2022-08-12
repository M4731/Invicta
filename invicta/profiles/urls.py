from django.urls import path
from profiles import views

app_name = 'profiles'

urlpatterns = [
    path('<slug:slug>/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('update/<slug:slug>/', views.ProfileUpdate.as_view(), name='profile_update'),
]
