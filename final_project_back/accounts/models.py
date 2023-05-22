from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Profile(models.Model):
    picture = models.ImageField(upload_to='images/', blank=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)