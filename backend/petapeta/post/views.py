from django.contrib.auth.models import AnonymousUser
from django.db import IntegrityError

from rest_framework import views

from core import models
from core import serializers

from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

class CreatePost(views.APIView):
    
    def post(self, request, *args, **kwargs):
        user = request.user
        
        if user is AnonymousUser:
            raise exceptions.AuthenticationFailed("ログインしてください。")
        
        title = request.data.get('title')
        content = request.data.get('content')
        urls = request.data.get('urls')
        
        post = models.Post(user=user, title=title, content=content, urls=urls)
        
        try:
            post.save()
        except Exception as e:
            print("Postデータの保存中にエラーが発生しました:", str(e))    

        serializer = serializers.PostSerializer(post)
        serialized_post = serializer.data
        serialized_post['urls'] = serialized_post['urls'].split(',')
        
        return Response(serialized_post, status=status.HTTP_201_CREATED)
        
class UploadImage(views.APIView):
    
    def post(self, request, *args, **kwargs):
        pass

class PostList(views.APIView):
    
    def get(self, request, *args, **kwargs):
        
        if request.user is AnonymousUser:
            raise exceptions.AuthenticationFailed("ログインしてください。")
        
        posts =  models.Post.objects.all()
        serializer = serializers.PostSerializer(posts, many=True)
        serialized_posts = serializer.data
        
        return Response(serialized_posts, status=status.HTTP_200_OK)
        
class PostIt(views.APIView):
    
    def post(self, request, post_id, *args, **kwargs):
        
        user = request.user
        
        if user is AnonymousUser:
            raise exceptions.AuthenticationFailed("ログインしてください。")
        
        post = models.Post.objects.get(id=post_id)
        
        sticy_note = models.StickyNote(user=user, post=post)
        
        try:
            sticy_note.save()
        except Exception as e:
            exceptions.APIException("Sticky Note データの保存中にエラーが発生しました:", str(e))
        
        serializer = serializers.StickyNoteSerializer(sticy_note)
        serialized_sticy_note = serializer.data
        
        return Response(serialized_sticy_note)
    
class UnPostIt(views.APIView):
    
    def delete(self, request, sticky_note_id,  *args, **kwargs):
        
        if request.user is AnonymousUser:
            raise exceptions.AuthenticationFailed("ログインしてください。")
        
        try:
            sticy_note = models.StickyNote.objects.get(id=sticky_note_id)
        except models.StickyNote.DoesNotExist:
            raise exceptions.NotFound("Sticky Note が見つかりませんでした。")
        
        try:
            sticy_note.delete()
        except Exception as e:
            exceptions.APIException("Sticky Note データの削除中にエラーが発生しました:", str(e))

        return Response(status=204)
        
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
        
        return Response(serialized_like)

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

        return Response(status=204)

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
        
        return Response(serialized_like)

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

        return Response(status=204)
    