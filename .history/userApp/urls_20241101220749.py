from django.urls import path
from .views import login_view

urlpatterns = [
    path('register/', UserCreateView.as , name='home'),
    path('login/', home, name='home'),
]