from django.urls import path
from .views import Sponsors_list,register_sponsorship

urlpatterns = [
    path('Sponsors_list', Sponsors_list, name='Sponsors_list'),
    path('register_sponsor', register_sponsorship, name='register_sponsor'),
    path('register_sponsor', register_sponsorship, name='register_sponsor'),
]