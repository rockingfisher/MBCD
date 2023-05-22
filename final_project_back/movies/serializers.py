from rest_framework import serializers
from .models import Movie
from .models import Genre


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('id','title','released_date','poster_path','overview','vote_avg','genres')
