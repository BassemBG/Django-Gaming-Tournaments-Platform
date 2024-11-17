from django.urls import path
from .views import register, ParticipationDeleteView

urlpatterns = [
    path('register_participation/', register, name='register_participation'),
    path('delete_participation/<int:pk>/', ParticipationDeleteView., name='delete_participation'),
]