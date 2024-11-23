from django.urls import path
from .views import Tournaments_View,completed_tournaments_view

urlpatterns = [
    path('Tournaments_View', Tournaments_View, name='Tournaments_View'),
    path('completed-tournaments/', completed_tournaments_view, name='completed_tournaments'),

]