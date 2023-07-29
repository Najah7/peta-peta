from django.urls import path
from . import views

urlpatterns = [
    # 一覧
    path("list/", views.PostList.as_view(), name="post-list"),
    # 投稿
    path('', views.CreatePost.as_view(), name='create-post'),
    # 詳細
    path('<int:pk>/', views.PostDetail.as_view(), name='post-detail'),

    
]