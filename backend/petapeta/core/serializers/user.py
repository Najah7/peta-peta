from rest_framework import serializers
from core.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = (
            'email',
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
            'updated_at',
            'created_at',
            'groups',
            'user_permissions',
            'last_login'
        )