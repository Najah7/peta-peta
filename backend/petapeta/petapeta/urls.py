"""
URL configuration for petapeta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include #includeのインポート

urlpatterns = [
    # 管理者や開発者用
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    
    # 認証関係
    path('', include('djoser.urls.authtoken')),
    
    # ユーザー
    path('me/', include('user.urls')),
    path('users/', include('user.urls')),
    path('follow/', include('follow.urls')),
    path('unfollow/', include('unfollow.urls')),
    
    # 投稿
    path('share-your-views/', include('post.urls')),
    path('posts/', include('post.urls')),
    path('upload/', include('upload.urls')),
    
    # その他の機能
    path('like/', include('like.urls')),
    path('unlike/', include('unlike.urls')),
    path('post-it/', include('post_it.urls')),
    path('unpost-it/', include('unpost_it.urls')),
]
