from django.urls import path
from lessons import views

app_name = 'lessons'

urlpatterns = [
    path('program/new/',views.CreateProgram.as_view(),name='create_program'),
    path('program/list/<str:username>',views.ListPrograms.as_view(),name='programs_list'),
]
