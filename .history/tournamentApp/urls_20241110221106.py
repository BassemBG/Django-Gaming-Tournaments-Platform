from django.urls import path
from .views import hoTournaments_Viewme

urlpatterns = [
    path('Tournaments_View', home, name='home'),
]