from rest_framework import serializers
from .models import Review, Comment


class ReviewListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only= True)

    class Meta:
        model = Review
        fields = ('id', 'title','content','user','username' )


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id','content','review_id')
        # read_only_fields = ('review_id',)

class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='review_set.count',read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Review
        fields = ('id', 'title','username','content','comment_set','comment_count','created_at','updated_at', 'rank', 'movie_title'  )