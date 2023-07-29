from django.contrib.auth.models import AnonymousUser

from rest_framework import views
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework import status

from core import models
from core import serializers




class PostIt(views.APIView):
    
    def post(self, request, post_id, *args, **kwargs):
        
        user = request.user
        
        if user is AnonymousUser:
            raise exceptions.AuthenticationFailed("ログインしてください。")
        
        post = models.Post.objects.get(id=post_id)
        
        sticky_note = models.StickyNote(user=user, post=post)
        
        try:
            sticky_note.save()
        except Exception as e:
            exceptions.APIException("Sticky Note データの保存中にエラーが発生しました:", str(e))
        
        serializer = serializers.StickyNoteSerializer(sticky_note)
        serialized_sticky_note = serializer.data
        
        return Response(serialized_sticky_note, status=status.HTTP_201_CREATED)
    

        
    