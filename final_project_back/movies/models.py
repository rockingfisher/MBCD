from django.db import models
from django.conf import settings

from accounts.models import User, Profile

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Movie(models.Model) :
    title = models.CharField(max_length=100)
    released_date = models.DateField()
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    genres = models.ManyToManyField(Genre)
    like_user = models.ManyToManyField(User, related_name='like_movie')
    

    def __str__(self):
        return self.title