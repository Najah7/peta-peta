from django.contrib.auth.models import AnonymousUser

from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

from core import models

class UnlikePost(views.APIView):
    
    def delete(self, request, id,  *args, **kwargs):
        user = request.user
        if user is AnonymousUser:
            exceptions.AuthenticationFailed("ログインしてください。")
        
        post = models.Post.objects.get(id=id)
        
        try:
            like = models.PostLike.objects.filter(post=post, user=user).first()
        except models.PostLike.DoesNotExist:
            raise exceptions.NotFound("Like が見つかりませんでした。")
        
        try:
            like.delete()
        except Exception as e:
            print("Like データの削除中にエラーが発生しました:", str(e))

        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UnlikeStickyNote(views.APIView):
    
    def delete(self, request, id, *args, **kwargs):
        user = request.user
        if user is AnonymousUser:
            raise exceptions.AuthenticationFailed("ログインしてください。")
        
        try:
            like = models.StickyNoteLike.objects.filter(id=id, user=user).get()
        except models.StickyNoteLike.DoesNotExist:
            raise exceptions.NotFound("Like が見つかりませんでした。")

        # if like is None:
        #     exceptions.NotFound("Like が見つかりませんでした。")
        
        try:
            like.delete()
        except Exception as e:
            raise exceptions.APIException("Like データの削除中にエラーが発生しました" + "Detail:" + str(e))

        return Response(status=status.HTTP_204_NO_CONTENT)