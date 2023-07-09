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
        
        posts = models.Post.objects.filter(user=user)
        sticky_notes = models.StickyNote.objects.filter(user=user)
        
        
        serializer = serializers.UserSerializer(user)
        serialized_user = serializer.data
        serializer = serializers.PostSerializer(posts, many=True)
        serialized_posts = serializer.data
        serializer = serializers.StickyNoteSerializer(sticky_notes, many=True)
        serializer_sticky_notes = serializer.data
        
        response = {
            'user': serialized_user,
            'posts': serialized_posts,
            'sticky_notes': serializer_sticky_notes
        }
        
        return Response(response, status=status.HTTP_200_OK)


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
    
class FollowUser(views.APIView):
    
    def post(self, request, user_id, format=None):
        user = request.user
        
        if user is AnonymousUser:
            raise exceptions.AuthenticationFailed('認証されていません')
        
        follower = models.CustomUser.objects.get(id=user_id)
        follow = models.Follow(followee=user, follower=follower)
        
        try:
            follow.save()
        except IntegrityError as e:
            response = {
                'message': 'すでにフォローしています。',
                'error': str(e)
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        serializer = serializers.FollowSerializer(follow)
        serialized_follow = serializer.data
        
        response = {
            "message": "フォローしました。",
            "follow_info": serialized_follow
            }
        
        return Response(response, status=status.HTTP_200_OK)

class UnFollowUser(views.APIView):
    
    def post(self, request, user_id, format=None):
        user = request.user
        
        if user is AnonymousUser:
            raise exceptions.AuthenticationFailed('認証されていません')
        
        try:
            follow = models.Follow.objects.get(followee=user, follower=user_id)
        except models.Follow.DoesNotExist:
            raise exceptions.NotFound('フォローしていません')

        try:
            follow.delete()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            print("削除中に異常が発生しました。" + 'detaile: ' + e)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
    