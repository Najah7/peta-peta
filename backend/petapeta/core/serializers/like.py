from rest_framework import serializers

from core.models import Like
from core.serializers import UserSerializer, PostSerializer

class LikeSerializer(serializers.Serializer):
    class Meta:
        model = Like
    
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)