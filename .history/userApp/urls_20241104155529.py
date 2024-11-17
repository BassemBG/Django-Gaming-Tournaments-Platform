from django.urls import path
from .views import register,CustomLoginView,UserDetailView,CustomLogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/<str:pk>/', UserDetailView.as_view(), name='profile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('up/', CustomLogoutView.as_view(), name='logout'),
]
