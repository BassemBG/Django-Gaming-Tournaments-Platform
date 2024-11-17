from django.urls import path
from .views import register,CustomLoginView,UserDetailView,CustomLogoutView,updateProfile

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', pr, name='profile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile_edit/<str:pk>/', updateProfile.as_view(), name='edit'),
]
