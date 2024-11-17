from django.urls import path
from .views import register,CustomLoginView,UserDetailView,CustomLogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/<str:pk>/', UserDetailView.as_view(), name='profile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile_edit/<str:pk>/', CustomLogoutView.as_view(), name='logout'),
]
