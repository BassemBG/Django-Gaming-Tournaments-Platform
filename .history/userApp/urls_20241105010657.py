from django.urls import path
from .views import register,CustomLoginView,profile_view,CustomLogoutView,update_user

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/<str:pk>/', profile_view, name='profile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile_edit/<str:pk>/', update_user, name='edit'),
]
