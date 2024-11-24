from django.urls import path
from .views import Tournaments_View

urlpatterns = [
    path('Tournaments_View', Tournaments_View, name='Tournaments_View'),
]