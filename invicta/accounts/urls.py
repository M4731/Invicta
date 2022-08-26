from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('login/',LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/student',views.StudentSignUpView.as_view(),name='signup_student'),
    path('signup/teacher',views.TeacherSignUpView.as_view(),name='signup_teacher'),
    path('update/student/<int:pk>',views.UserUpdateView.as_view(),name='update_user'),
    path('update/teacher/<int:pk>',views.TeacherUpdateView.as_view(),name='update_teacher'),
    path('update/teacher-info/<int:pk>',views.TeacherInfoUpdateView.as_view(),name='update_teacher_info'),
]