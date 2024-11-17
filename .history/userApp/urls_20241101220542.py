from django.urls import path
from .views import lo

urlpatterns = [
    path('register/', home, name='home'),
    path('login/', home, name='home'),
]