from django.urls import path
from .views import Sponsors_list

urlpatterns = [
    path('', home, name='home'),
]