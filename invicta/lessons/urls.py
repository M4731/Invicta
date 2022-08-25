from django.urls import path
from lessons import views

app_name = 'lessons'

urlpatterns = [
    path('<int:pk>/create/', views.CreateLesson.as_view(), name='create_lesson'),
    path('t/<int:pk>/', views.TeacherLessons.as_view(), name='appending_lessons'),
    path('s/<int:pk>/', views.StudentLessons.as_view(), name='student_lessons'),
    path('deny/<int:pk>/',views.DeleteLesson.as_view(), name='delete_lesson'),
]
