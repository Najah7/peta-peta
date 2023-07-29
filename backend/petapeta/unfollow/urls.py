from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.UnFollowUser.as_view(), name='unfollow_user'),
]