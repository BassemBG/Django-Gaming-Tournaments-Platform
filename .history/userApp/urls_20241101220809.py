from django.urls import path
from .views import UserCreateView

urlpatterns = [
    path('register/', UserCreateView.as_view() , name='register_user'),
    path('register/', UserCreateView.as_view() , name='login'),
    path('login/', home, name='home'),
]