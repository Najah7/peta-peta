from django.db import models
from django.utils import timezone
# Create your models here.

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name= models.CharField(max_length=100)
    icon= models.URLField(blank=True)
    comment= models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

#Post Model
class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id= models.ForeignKey('Users', on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    content=models.CharField(max_length=100)

#Likes Model

#Follows Model

#Posts Model