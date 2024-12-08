from django.urls import path
from . import views

urlpatterns = [
    path('openai-query/', views.openai_query_view, name='openai_query'),
]