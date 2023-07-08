from rest_framework import serializers

from core.models import Follow
from core.serializers import UserSerializer

class FollowSerializer(serializers.Serializer):
    class Meta:
        model = Follow
        
    id = serializers.IntegerField(read_only=True)
    follower = UserSerializer(read_only=True)
    followee = UserSerializer(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)