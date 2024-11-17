from django.urls import path
from .views import register

urlpatterns = [
    path('register_participation/', register, name='register_participation'),
    path('delete_participation/<int:pk>/', register, name='register_participation'),
]