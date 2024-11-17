from django.urls import path
from .views import Tournaments_View

urlpatterns = [
    path('Games_list', Tournaments_View, name='Games_list'),
]