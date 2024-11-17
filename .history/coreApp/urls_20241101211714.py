from django.urls import path
from .views import home

urlpatterns = [
    path('admin/', home, name='home'),
]