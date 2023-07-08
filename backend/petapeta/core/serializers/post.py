from rest_framework import serializers

from core.models import Post
from core.serializers import UserSerializer

class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
    
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    title = serializers.CharField(max_length=30)
    content = serializers.CharField(max_length=1024)
    url = serializers.CharField()
        