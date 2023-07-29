from django.contrib.auth.models import AnonymousUser

from rest_framework import views

from core import models

from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

class UnPostIt(views.APIView):
    
    def delete(self, request, sticky_note_id,  *args, **kwargs):
        
        if request.user is AnonymousUser:
            raise exceptions.AuthenticationFailed("ログインしてください。")
        
        try:
            sticky_note = models.StickyNote.objects.get(id=sticky_note_id)
        except models.StickyNote.DoesNotExist:
            raise exceptions.NotFound("Sticky Note が見つかりませんでした。")
        
        try:
            sticky_note.delete()
        except Exception as e:
            exceptions.APIException("Sticky Note データの削除中にエラーが発生しました:", str(e))

        return Response(status=status.HTTP_204_NO_CONTENT)