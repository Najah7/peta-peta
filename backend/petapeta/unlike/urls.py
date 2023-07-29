from django.urls import path
from . import views

urlpatterns = [
    # 投稿
    path("post/<int:id>", views.UnlikePost.as_view(), name="unlike-post"),
    # 付箋
    path("sticky-note/<int:id>", views.UnlikeStickyNote.as_view(), name="unlike-sticky-note"),
]