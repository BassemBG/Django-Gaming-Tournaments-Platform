from django.urls import path
from .views import home

urlpatterns = [
    path('tournaments', home, name='home'),
]