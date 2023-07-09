from rest_framework import serializers

from core.models import StickyNote
from core.serializers import UserSerializer, PostSerializer

class StickyNoteSerializer(serializers.Serializer):
    class Meta:
        model = StickyNote
    
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)