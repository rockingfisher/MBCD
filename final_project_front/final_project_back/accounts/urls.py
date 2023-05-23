from django.urls import path
from . import views



urlpatterns = [
    path('profile/<int:pk>/', views.profile),
    path('profilecreate/<int:pk>/', views.profilecreate),
    path('profile/increasecount/<int:pk>/<int:genre_id>/', views.increment_count),
    path('profile/increasecount/option/<int:pk>/<int:genre_id>/<int:score>/', views.increment_count_option),
    path('profile/togglecount/<int:pk>/<int:genre_id>/', views.toggle_key),
]
