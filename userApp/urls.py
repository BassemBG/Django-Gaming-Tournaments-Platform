from django.urls import path
from .views import register,CustomLoginView,profile_view,CustomLogoutView,update_user,view_participation,view_sponsorships,download_contract

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/<str:pk>/', profile_view, name='profile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('update_user/<str:pk>/', update_user, name='update_user'),
    path('participationList/<str:pk>/', view_participation, name='participationList'),
    path('sponsorshipList/<str:pk>/', view_sponsorships, name='sponsorshipList'),
    path('download_contract/<int:id>/', download_contract, name='download_contract'),
]
