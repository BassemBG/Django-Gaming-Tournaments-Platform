from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('login/', home, name='home'),
    path('register/', UserCreateView.as_view() , name='register'),
    path('register/', UserCreateView.as_view() , name='login'),
    
]