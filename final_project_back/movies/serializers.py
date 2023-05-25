from rest_framework import serializers
from .models import Movie
from .models import Genre


class MovieSerializer(serializers.ModelSerializer):
    like_user = serializers.SerializerMethodField()

    def get_like_user(self, obj):
        like_users = obj.like_user.all()
        serialized_users = [{"id": user.id, "username": user.username} for user in like_users]
        return serialized_users
        
    class Meta:
        model = Movie
        fields = ('id','title','released_date','poster_path','overview','vote_avg','genres','total_score','like_user')
