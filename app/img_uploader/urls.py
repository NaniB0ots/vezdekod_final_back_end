from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:pk>/', views.ShowImageView.as_view()),
    path('', views.UploadImageView.as_view()),
]
