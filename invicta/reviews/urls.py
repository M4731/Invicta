from django.urls import path
from reviews import views

app_name = 'reviews'

urlpatterns = [
    path('<int:pk>/create/', views.CreateReview.as_view(), name='create_review'),
    path('sr/<int:pk>/', views.StudentReviews.as_view(), name='student_reviews'),
    path('sr/delete/<int:pk>/',views.DeleteReview.as_view(), name='delete_review'),
    path('sr/update/<int:pk>/',views.UpdateReview.as_view(), name='update_review'),
    path('pr/<int:pk>/', views.TeacherReviews.as_view(), name='teacher_reviews'),
]
