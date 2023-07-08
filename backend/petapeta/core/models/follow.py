'''
Follow Model

概要: UserとUserの中間テーブル

'''

from django.db import models

from django.conf import settings

class Follow(models.Model):
    
    class Meta:
        db_table = 'follows'
    
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='following', on_delete=models.CASCADE)
    followee = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='followers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.follower.name + 'が' + self.followed.name + 'をフォローしてます。'
