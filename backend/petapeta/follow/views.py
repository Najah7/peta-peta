from django.contrib.auth.models import AnonymousUser
from django.db import IntegrityError

from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

from core import models
from core import serializers

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