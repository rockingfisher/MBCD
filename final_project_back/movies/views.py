from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.shortcuts import get_object_or_404
from .serializers import MovieSerializer
from .models import Movie
from datetime import datetime
from django.contrib.auth.decorators import login_required
from accounts.models import User, Profile

            
@api_view(['GET'])
def movie(request) :
    if request.method == 'GET' :
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST','PUT'])
def takeGenre(request): 
    if request.method == 'GET':
        movieURL = f'https://api.themoviedb.org/3/discover/movie?api_key=f433951fa3f9ea7fc5b7f38dbec9ac20&language=ko-KR'
        genreURL = f'https://api.themoviedb.org/3/genre/movie/list?api_key=f433951fa3f9ea7fc5b7f38dbec9ac20&language=ko'
        genreList = requests.get(genreURL).json()
        movieList = requests.get(movieURL).json()
        genre = genreList.get('genres')
        
    return Response(genre)

@api_view(['GET','POST'])
def likes(request, movie_id):
    likemovie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        user = request.user
        if likemovie.like_user.filter(pk=user.pk).exists():
            likemovie.like_user.remove(user.pk)
        else:
            likemovie.like_user.add(user.pk)
    serializer = MovieSerializer(likemovie)
    return Response(serializer.data)



