'''
Phote Model

概要：投稿の画像モデル
'''

from django.db import models
from core.models import Post

class Phote(models.Model):
    
    class Meta:
        db_table = 'photes'
    
    id = models.IntegerField(primary_key=True)
    post = models.ForeignKey(Post, related_name='photes', on_delete=models.CASCADE)
    # 後々S３に移行。
    image = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.post.tile + 'の画像'