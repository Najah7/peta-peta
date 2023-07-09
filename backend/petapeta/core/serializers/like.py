from rest_framework import serializers

from core.models import PostLike, StickyNoteLike
from core.serializers import UserSerializer, PostSerializer, StickyNoteSerializer

class PostLikeSerializer(serializers.Serializer):
    class Meta:
        model = PostLike
        unique_together = ('user', 'post')
    
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    
class StickyNoteLikeSerializer(serializers.Serializer):
    class Meta:
        model = StickyNoteLike
    
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    sticky_note = StickyNoteSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)