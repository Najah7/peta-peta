'''
Like Model

概要: UserとPostの中間テーブル

'''

from django.db import models

from core.models import Post

from django.conf import settings
class Like(models.Model):
    class Meta:
        db_table = 'likes'
    
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user.name + 'が' + self.post.title + 'をいいねしてます。'