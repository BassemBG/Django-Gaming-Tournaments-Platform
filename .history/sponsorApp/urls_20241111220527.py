from django.urls import path
from .views import Sponsors_list

urlpatterns = [
    path('Sponsors_list', Sponsors_list, name='Sponsors_list'),
    path('Sponsors_list', Sponsors_list, name='register_sponsor'),
]