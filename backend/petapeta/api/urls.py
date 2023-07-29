#path関数をインポート
from django.urls import path
# 同ディレクトリからview.pyをインポート
from . import views

urlpatterns = [
    path('health/', views.healthcheck, name='health'),
]