from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', UserCreateView.as_view() , name='register'),
    path('register/', UserCreateView.as_view() , name='login'),
    
]