from django.urls import path
from . import views

urlpatterns = [
    path('share-your-views/', views.CreatePost.as_view(), name='create-post'),
    # path("upload-image/", views.UploadImage.as_view(), name="upload-image"),
    path("list/", views.PostList.as_view(), name="post-list"),
    path("post-it/<int:post_id>/", views.PostIt.as_view(), name="post-detail"),
    path("unpost-it/<int:sticky_note_id>/", views.UnPostIt.as_view(), name="post-detail"),
    # path("like/<int:post_id>/", views.LikePost.as_view(), name="like-post"),
    # path("unlkike/<int:post_id>/", views.UnlikePost.as_view(), name="unlike-post"),
    # path("like/<int:sticky_note_id>/", views.LikeStickyNote.as_view(), name="like-sticky-note"),
    # path("unlike/<int:sticky_note_id>/", views.UnlikeStickyNote.as_view(), name="unlike-sticky-note"),
]