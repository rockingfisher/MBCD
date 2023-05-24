from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import HttpResponse


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

GENRES = {
28: 'action',
12: 'adventure',
16: 'animation',
35: 'comedy',
80: 'crime',
99: 'documentary',
18: 'drama',
10751: 'family',
14: 'fantasy',
36: 'history',
27: 'horror',
10402: 'music',
9648: 'mystery',
10749: 'romance',
878: 'science_fiction',
10770: 'tv_movie',
53: 'thriller',
10752: 'war',
37: 'western'
}

# 방문 횟수에 따라 +1 점을 추가한다.
def increment_count(request, pk, genre_id):
    field_name = GENRES[genre_id] 
    profile = get_object_or_404(Profile, user_id=pk)
    setattr(profile, f'{field_name}_cnt', getattr(profile, f'{field_name}_cnt') + 1)
    profile.save()
    return HttpResponse(f"{field_name} count incremented successfully!")

# 원하는 점수를 추가한다.
def increment_count_option(request, pk, genre_id, score):
    field_name = GENRES[genre_id] 
    profile = get_object_or_404(Profile, user_id=pk)
    setattr(profile, f'{field_name}_cnt', getattr(profile, f'{field_name}_cnt') + score)
    profile.save()
    return HttpResponse(f"{field_name} count incremented successfully!")


# 해당 키 값을 변경하면 해당 장르의 점수가 10점 오르거나 내린다. 기본은 10점임으로 +10, 0로 볼 수 있다.
def toggle_key(request, pk, genre_id):
    profile = get_object_or_404(Profile, user_id=pk)
    genre = GENRES[genre_id]
    # 키에 해당하는 불리안 속성 가져오기
    key_field = getattr(profile, f"{genre}_key")
    
    # 속성 토글 및 _cnt 속성 증가
    if key_field:
        key_field = False
        setattr(profile, f"{genre}_key", key_field)
        setattr(profile, f"{genre}_cnt", getattr(profile, f"{genre}_cnt") - 10)
    else:
        key_field = True
        setattr(profile, f"{genre}_key", key_field)
        setattr(profile, f"{genre}_cnt", getattr(profile, f"{genre}_cnt") + 10)

    # 변경사항 저장
    profile.save()

    return HttpResponse(f"{key_field} Key toggled successfully!")
