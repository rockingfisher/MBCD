from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.movie),
    path('genre/', views.takeGenre),
]