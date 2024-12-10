from django.urls import path
from .views import process_voice_command,voice_debug_page

urlpatterns = [
    path("voice-command/", process_voice_command, name="process_voice_command"),
    path("voice-debug/", voice_debug_page, name="voice_debug_page"),
]
