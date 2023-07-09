from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShowProfile.as_view(), name='show_profile'),
    path('create/', views.CreateUser.as_view(), name='create_user'),
    path('list/', views.UserList.as_view(), name='user_list'),
    path('follow/<int:user_id>/', views.FollowUser.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', views.UnFollowUser.as_view(), name='unfollow_user'),
]