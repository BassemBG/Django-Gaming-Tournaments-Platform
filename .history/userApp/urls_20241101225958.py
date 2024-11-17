from django.urls import path
from .views import register,CustomLoginView,UserDetailView

urlpatterns = [
    path('register/', register , name='register'),
    path('login/', CustomLoginView.as_view() , name='login'),
    path('profile/< pk:int >', UserDetailView.as_view() , name='pri'),
    
]