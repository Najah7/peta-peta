from django.contrib.auth.models import AnonymousUser

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
        
class PostList(views.APIView):
    
    def get(self, request, *args, **kwargs):
        
        if request.user is AnonymousUser:
            raise exceptions.AuthenticationFailed("ログインしてください。")
        
        posts =  models.Post.objects.all()
        serializer = serializers.PostSerializer(posts, many=True)
        serialized_posts = serializer.data
        
        return Response(serialized_posts, status=status.HTTP_200_OK)
        
class PostDetail(views.APIView):
    
    def get(self, request, pk, *args, **kwargs):
        
        if request.user is AnonymousUser:
            raise exceptions.AuthenticationFailed("ログインしてください。")
        
        post = models.Post.objects.get(pk=pk)
        serializer = serializers.PostSerializer(post)
        serialized_post = serializer.data
        
        return Response(serialized_post, status=status.HTTP_200_OK)