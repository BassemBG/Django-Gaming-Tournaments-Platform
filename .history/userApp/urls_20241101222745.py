from django.urls import path
from .views import UserCreateView,CustomLoginView

urlpatterns = [
    path('register/', register.as_view() , name='register'),
    path('login/', CustomLoginView.as_view() , name='login'),
    
]