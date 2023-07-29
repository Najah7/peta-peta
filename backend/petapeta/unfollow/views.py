from django.contrib.auth.models import AnonymousUser

from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

from core import models

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