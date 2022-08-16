from django.urls import path
from lessons import views

app_name = 'lessons'

urlpatterns = [
    path('<int:pk>/create/', views.CreateLesson.as_view(), name='create_lesson'),
]
