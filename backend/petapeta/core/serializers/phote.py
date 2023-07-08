from rest_framework import serializers

from core.models import Phote

from core.serializers import PostSerializer

class PhoteSerializer(serializers.Serializer):
    class Meta:
        model = Phote
        
    id = serializers.IntegerField(read_only=True)
    post = PostSerializer(read_only=True)
    image = serializers.ImageField()