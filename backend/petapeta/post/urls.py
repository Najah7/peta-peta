from django.urls import path
from . import views

urlpatterns = [
    path('share-your-views/', views.CreatePost.as_view(), name='create-post'),
    path("upload-image/", views.UploadImage.as_view(), name="upload-image"),
    path("list/", views.PostList.as_view(), name="post-list"),
    path("post-it/<int:post_id>/", views.PostIt.as_view(), name="post-detail"),
    path("unpost-it/<int:sticky_note_id>/", views.UnPostIt.as_view(), name="post-detail"),
    path("like/post/<int:id>", views.LikePost.as_view(), name="like-post"),
    path("unlike/post/<int:id>", views.UnlikePost.as_view(), name="unlike-post"),
    path("like/sticky-note/<int:id>", views.LikeStickyNote.as_view(), name="like-sticky-note"),
    path("unlike/sticky-note/<int:id>", views.UnlikeStickyNote.as_view(), name="unlike-sticky-note"),
]