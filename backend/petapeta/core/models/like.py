'''
Like Model

概要: UserとPostの中間テーブル

'''

from django.db import models

from core.models import Post, StickyNote

from django.conf import settings
class PostLike(models.Model):
    class Meta:
        db_table = 'post_likes'
        unique_together = ('user', 'post')
    
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user.name + 'が' + self.post.title + 'をいいねしてます。'

class StickyNoteLike(models.Model):
    class Meta:
        db_table = 'sticky_note_likes'
        unique_together = ('user', 'sticky_note')
    
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes', on_delete=models.CASCADE)
    sticky_note = models.ForeignKey(StickyNote, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.user.name + 'が' + self.post.title + 'をいいねしてます。'