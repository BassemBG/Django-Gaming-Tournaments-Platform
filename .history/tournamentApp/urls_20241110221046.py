from django.urls import path
from .views import home

urlpatterns = [
    path('Tournaments_View', home, name='home'),
]