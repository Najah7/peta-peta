from django.contrib.auth.models import AnonymousUser
from django.core.paginator import Paginator
from django.db import IntegrityError

from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

from core import models
from core import serializers



class ShowProfile(views.APIView):
    def get(self, request, format=None):
        user = request.user
        
        if user is AnonymousUser:
            raise exceptions.AuthenticationFailed('認証されていません')
        
        # データを取得
        posts = models.Post.objects.filter(user=user)
        sticky_notes = models.StickyNote.objects.filter(user=user)
        followers = models.Follow.objects.filter(followee=user)
        followings = models.Follow.objects.filter(follower=user)
        
        # データの量を制限
        if len(sticky_notes) > 30:
            sticky_notes = sticky_notes[:30]
        if len(followers) > 10:
            followers[:10]
        if len(followings) > 10:
            followings[:10]
        
        # シリアライズ
        serializer = serializers.UserSerializer(user)
        serialized_user = serializer.data
        serializer = serializers.PostSerializer(posts, many=True)
        serialized_posts = serializer.data
        serializer = serializers.StickyNoteSerializer(sticky_notes, many=True)
        serialized_sticky_notes = serializer.data
        serializer = serializers.FollowSerializer(followers, many=True)
        serialized_followers = serializer.data
        serializer = serializers.FollowSerializer(followings, many=True)
        serialized_followeings = serializer.data
        
        # レスポンス
        return Response({
            'user': serialized_user,
            'posts': serialized_posts,
            'sticky_notes': serialized_sticky_notes,
            'followers': serialized_followers,
            'followings': serialized_followeings,
        }, status=status.HTTP_200_OK)
        


class CreateUser(views.APIView):
    
    def post(self, request, format=None):
        user = models.CustomUser.objects.create_user(
            email=request.data['email'],
            password=request.data['password'],
            name=request.data['username'],
        )
        
        serializer = serializers.UserSerializer(user)
        serialized_user = serializer.data
        
        response = {
            "message": "ユーザーの作成に成功しました",
            "user": serialized_user
        }
        
        return Response(response, status=status.HTTP_201_CREATED)

class UserList(views.APIView):
    
    def get(self, request, format=None):
        
        user = request.user
        if user is AnonymousUser:
            raise exceptions.AuthenticationFailed('認証されていません')
        
        page_number = request.query_params.get('page')
        
        if page_number is None:
            page_number = 1
        
        users = models.CustomUser.objects.all()
        users_paginator = Paginator(users, 10)
        
        
        
        current_users = users_paginator.get_page(page_number)
        
        serializer = serializers.UserSerializer(current_users, many=True)
        serialized_user = serializer.data
        
        return Response(serialized_user, status=status.HTTP_200_OK)
    
        
    