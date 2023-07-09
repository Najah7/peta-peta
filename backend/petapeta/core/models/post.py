'''
Post Model

概要：投稿を管理するモデル
'''

from django.db import models

from django.conf import settings

class Post(models.Model):
    class Meta:
        db_table = 'posts'
    
    user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    content=models.CharField(max_length=1024)
    # URLのカンマ区切り👇
    urls = models.TextField()
    
    def __str__(self) -> str:
        return self.title