from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def profile(request, pk):
    profile = get_object_or_404(Profile, user_id=pk)
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfileSerializer(profile, data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)


@api_view(['POST'])
def profilecreate(request, pk):
    serializer = ProfileSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user_id=pk)
        return Response(serializer.data)