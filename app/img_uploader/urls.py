from django.urls import path

from . import views

urlpatterns = [
    path('get/<str:pk>/', views.ShowImageView.as_view()),
    path('upload/', views.UploadImageView.as_view()),
]
