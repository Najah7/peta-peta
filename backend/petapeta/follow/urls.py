from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/', views.FollowUser.as_view(), name='follow_user'),
]