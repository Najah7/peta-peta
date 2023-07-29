from django.urls import path
from . import views

urlpatterns = [
    path("image/", views.UploadImage.as_view(), name="upload-image"),
]