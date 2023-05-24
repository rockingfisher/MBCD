from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.movie),
    path('genre/', views.takeGenre),
    # path('search/', views.movieSearch)
    path('<int:movie_id>/likes/', views.likes)
]