from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404

from accounts.models import User

from .models import Comment , Review
from . serializers import ReviewSerializer, CommentSerializer, ReviewListSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def review_list(request) :

    # user = get_object_or_404(User, pk=1)

    if request.method == 'GET' :
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST' :
        user_pk = request.data.get('user_pk')
        user = get_object_or_404(User, pk=user_pk)
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    # 만든 유저만 수정 가능 
    # if not request.user.review_set.filter(pk=review_pk).exists():
    #     return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDON)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE' :
        review.delete()
        return Response({ 'id': review_pk}, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)



@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    

@api_view(['POST'])
def comment_create(request, review_pk):
    # review = Review.objects.get(pk=review_pk)
    review = get_object_or_404(Review, pk=review_pk)
    user = get_object_or_404(User, pk=1)

    # comment = get_object_or_404(Comment)

    serializer = CommentSerializer(data=request.data)
    # print(">>>>>>>>>")
    if serializer.is_valid(raise_exception=True):
        serializer.save(review_id=review, user_id=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)