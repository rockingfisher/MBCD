from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Profile(models.Model):
    picture = models.ImageField(upload_to='images/', blank=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    action_cnt = models.IntegerField(default=0)
    adventure_cnt = models.IntegerField(default=0)
    animation_cnt = models.IntegerField(default=0)
    comedy_cnt = models.IntegerField(default=0)
    crime_cnt = models.IntegerField(default=0)
    documentary_cnt = models.IntegerField(default=0)
    drama_cnt = models.IntegerField(default=0)
    family_cnt = models.IntegerField(default=0)
    fantasy_cnt = models.IntegerField(default=0)
    history_cnt = models.IntegerField(default=0)
    horror_cnt = models.IntegerField(default=0)
    music_cnt = models.IntegerField(default=0)
    mystery_cnt = models.IntegerField(default=0)
    romance_cnt = models.IntegerField(default=0)
    science_fiction_cnt = models.IntegerField(default=0)
    tv_movie_cnt = models.IntegerField(default=0)
    thriller_cnt = models.IntegerField(default=0)
    war_cnt = models.IntegerField(default=0)
    western_cnt = models.IntegerField(default=0)
       
    action_key = models.BooleanField(default=False)
    adventure_key = models.BooleanField(default=False)
    animation_key = models.BooleanField(default=False)
    comedy_key = models.BooleanField(default=False)
    crime_key = models.BooleanField(default=False)
    documentary_key = models.BooleanField(default=False)
    drama_key = models.BooleanField(default=False)
    family_key = models.BooleanField(default=False)
    fantasy_key = models.BooleanField(default=False)
    history_key = models.BooleanField(default=False)
    horror_key = models.BooleanField(default=False)
    music_key = models.BooleanField(default=False)
    mystery_key = models.BooleanField(default=False)
    romance_key = models.BooleanField(default=False)
    science_fiction_key = models.BooleanField(default=False)
    tv_movie_key = models.BooleanField(default=False)
    thriller_key = models.BooleanField(default=False)
    war_key = models.BooleanField(default=False)
    western_key = models.BooleanField(default=False)