from django.urls import path
from .views import process_voice_command, redirect_based_on_command, voice_debug_page

urlpatterns = [
    path("voice-command/", process_voice_command, name="process_voice_command"),
    path("voice-command-redirect/", redirect_based_on_command, name="redirect_based_on_command"),
    path("voice-debug/", voice_debug_page, name="voice_debug_page"),
]