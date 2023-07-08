from rest_framework import views

from core import models
from core import serializers

from rest_framework.response import Response

class CreatePost(views.APIView):
    
    def post(self, request, *args, **kwargs):
        user = request.user
        title = request.data.get('title')
        content = request.data.get('content')
        urls = request.data.get('urls')
        
        if urls is not None:
            urls.split(',')
        
        post = models.Post(user=user, title=title, content=content, urls=urls)
        
        try:
            post.save()
        except Exception as e:
            print("Postデータの保存中にエラーが発生しました:", str(e))    

        serializer = serializers.PostSerializer(post)
        
        return Response(serializer.data)
        
class UploadImage(views.APIView):
    
    def post(self, request, *args, **kwargs):
        pass

class PostList(views.APIView):
    
    def get(self, request, *args, **kwargs):
        posts =  models.Post.objects.all()
        serializer = serializers.PostSerializer(posts, many=True)
        serialized_posts = serializer.data
        
        return Response(serialized_posts)
        
class PostIt(views.APIView):
    
    def post(self, request, *args, **kwargs):
        post_id = request.query_params.get('post_id')
        
        post = models.Post.objects.get(id=post_id)
        
        sticy_note = models.StickyNote(user=request.user, post=post)
        
        try:
            sticy_note.save()
        except Exception as e:
            print("Sticky Note データの保存中にエラーが発生しました:", str(e))
        
        serializer = serializers.StickyNoteSerializer(sticy_note)
        serialized_sticy_note = serializer.data
        
        return Response(serialized_sticy_note)
    
class UnPostIt(views.APIView):
    
    def delete(self, request, *args, **kwargs):
        sticy_note_id = request.query_params.get('sticy_note_id')
        
        sticy_note = models.StickyNote.objects.get(id=sticy_note_id)
        
        try:
            sticy_note.delete()
        except Exception as e:
            print("Sticky Note データの削除中にエラーが発生しました:", str(e))

        return Response(status=204)
        
class LikePost(views.APIView):
    
    def post(self, request, *args, **kwargs):
        post_id = request.query_params.get('post_id')
        
        post = models.Post.objects.get(id=post_id)
        
        like = models.Like(user=request.user, post=post)
        
        try:
            like.save()
        except Exception as e:
            print("Like データの保存中にエラーが発生しました:", str(e))
        
        serializer = serializers.LikeSerializer(like)
        serialized_like = serializer.data
        
        return Response(serialized_like)

class UnlikePost(views.APIView):
    
    def delete(self, request, *args, **kwargs):
        post_id = request.query_params.get('post_id')
        
        like = models.Like.objects.where(post_id=post_id).where(user=request.user).first()
        
        try:
            like.delete()
        except Exception as e:
            print("Like データの削除中にエラーが発生しました:", str(e))

        return Response(status=204)

class LikeStickyNote(views.APIView):
    
    def post(self, request, *args, **kwargs):
        sticy_note_id = request.query_params.get('sticy_note_id')
        
        sticy_note = models.StickyNote.objects.get(id=sticy_note_id)
        
        like = models.Like(user=request.user, sticy_note=sticy_note)
        
        try:
            like.save()
        except Exception as e:
            print("Like データの保存中にエラーが発生しました:", str(e))
        
        serializer = serializers.LikeSerializer(like)
        serialized_like = serializer.data
        
        return Response(serialized_like)

class UnlikeStickyNote(views.APIView):
    
    def delete(self, request, *args, **kwargs):
        sticy_note_id = request.query_params.get('sticy_note_id')
        
        like = models.Like.objects.where(sticy_note_id=sticy_note_id).where(user=request.user).first()
        
        try:
            like.delete()
        except Exception as e:
            print("Like データの削除中にエラーが発生しました:", str(e))

        return Response(status=204)
    