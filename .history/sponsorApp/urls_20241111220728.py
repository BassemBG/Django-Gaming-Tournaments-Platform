from django.urls import path
from .views import Sponsors_list,register_sponsor

urlpatterns = [
    path('Sponsors_list', Sponsors_list, name='Sponsors_list')
]