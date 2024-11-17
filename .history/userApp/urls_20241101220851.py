from django.urls import path
from .views import UserCreateView,CustomLoginView

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', UserCreateView.as_view() , name='register'),
    path('login/', CustomLoginView.as_view() , name='login'),
    
]