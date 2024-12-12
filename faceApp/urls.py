from django.contrib import admin
from django.urls import path
from .views import face_recognition_video

urlpatterns = [
    path('face/',face_recognition_video, name='face_recognition_video'),
]
