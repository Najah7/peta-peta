from django.urls import path
from . import views

urlpatterns = [
    # 付箋作成
    path("<int:post_id>/", views.PostIt.as_view(), name="post-detail"),
    path("<int:sticky_note_id>/", views.UnPostIt.as_view(), name="post-detail"),
]