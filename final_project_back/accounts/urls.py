from django.urls import path
from . import views



urlpatterns = [
    path('profile/<int:pk>/', views.profile),
    path('profilecreate/<int:pk>/', views.profilecreate),
]
