from django.urls import path
from . import views

urlpatterns = [
    # 投稿をLike
    path("post/<int:id>", views.LikePost.as_view(), name="like-post"),
    
    # 付箋をLike
    path("sticky-note/<int:id>", views.LikeStickyNote.as_view(), name="like-sticky-note"),
]

