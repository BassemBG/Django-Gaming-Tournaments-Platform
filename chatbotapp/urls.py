from django.urls import path
from . import views

urlpatterns = [
    path('openai-query/', views.chatbot_query_view, name='chatbot_query'),
]