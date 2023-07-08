'''
StickyNote Model

概要：付箋のモデル
'''

from django.db import models
from core.models import Post
from django.conf import settings

class StickyNote(models.Model):
    
    class Meta:
        db_table = 'sticky_notes'
    
    id = models.IntegerField(primary_key=True)
    user= models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sticky_notes', on_delete=models.CASCADE)
    post= models.ForeignKey(Post, related_name='sticky_notes', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.name + 'から' + self.post.title + 'への付箋'