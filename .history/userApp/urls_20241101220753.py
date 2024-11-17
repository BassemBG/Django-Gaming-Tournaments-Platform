from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('register/', UserCreateView.asv , name='home'),
    path('login/', home, name='home'),
]