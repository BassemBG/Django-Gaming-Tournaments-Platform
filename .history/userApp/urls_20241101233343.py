from django.urls import path
from .views import register,CustomLoginView,UserDetailView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/<str:pk>/', UserDetailView.as_view(), name='profile'),
    path(())
]
