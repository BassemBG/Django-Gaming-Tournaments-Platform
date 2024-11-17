from django.urls import path
from .views import Games_list
Games_list
urlpatterns = [
    path('Games_list', Tournaments_View, name='Games_list'),
]