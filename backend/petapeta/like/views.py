from django.contrib.auth.models import AnonymousUser
from django.db import IntegrityError

from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

from core import models
from core import serializers



# Create your views here.
class LikePost(views.APIView):
    
    def post(self, request, id,  *args, **kwargs):
        
        user = request.user
        if user is AnonymousUser:
            exceptions.AuthenticationFailed("ログインしてください。")
        
        try:
            post = models.Post.objects.get(id=id)
        except models.Post.DoesNotExist:
            exceptions.NotFound("Post が見つかりませんでした。")
        
        like = models.PostLike(user=user, post=post)
        
        try:
            like.save()
        except IntegrityError as e:
            raise exceptions.APIException("すでにLikeしています。" + "Detail: " + str(e), status.HTTP_400_BAD_REQUEST)
        
        serializer = serializers.PostLikeSerializer(like)
        serialized_like = serializer.data
        
        serialized_like['post']['urls'] = serialized_like['post']['urls'].split(',')
        
        return Response(serialized_like, status.HTTP_201_CREATED)



class LikeStickyNote(views.APIView):
    
    def post(self, request, id, *args, **kwargs):
        
        user = request.user
        if user is AnonymousUser:
            raise exceptions.AuthenticationFailed("ログインしてください。")
        
        try:
            sticky_note = models.StickyNote.objects.get(id=id)
        except models.StickyNote.DoesNotExist:
            raise exceptions.NotFound("Sticky Note が見つかりませんでした。")
        
        like = models.StickyNoteLike(user=user, sticky_note=sticky_note)
        
        try:
            like.save()
        except IntegrityError as e:
            raise exceptions.APIException("すでにLikeしています。" + "Detail: " + str(e), status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise exceptions.APIException("Like データの保存中にエラーが発生しました:", str(e))
        
        serializer = serializers.StickyNoteLikeSerializer(like)
        serialized_like = serializer.data
        
        return Response(serialized_like, status.HTTP_201_CREATED)

