from django.urls import path
from . import views

urlpatterns = [
    path("<int:sticky_note_id>/", views.UnPostIt.as_view(), name="post-detail"),
]