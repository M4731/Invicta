from django.urls import path
from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('<int:pk>/create/', views.CreateReview.as_view(), name='create_review'),
]
