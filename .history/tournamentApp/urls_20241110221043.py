from django.urls import path
from .views import home

urlpatterns = [
    path('tournaments_View', home, name='home'),
]