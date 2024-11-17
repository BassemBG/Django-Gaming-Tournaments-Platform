from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('register/', UserCreateView.as , name='home'),
    path('login/', home, name='home'),
]