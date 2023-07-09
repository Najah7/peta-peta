'''
User Model

概要：ユーザー情報を管理するモデル
'''

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    """ユーザーのオブジェクトマネージャー"""
    
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """カスタムユーザーモデル"""
    
    class Meta:
        db_table = 'users'
    
    name = models.CharField(max_length=255, default='名無し')
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    icon = models.URLField(blank=True)
    one_line_intro = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    
    def __str__(self) -> str:
        return self.name + 'さん'
    