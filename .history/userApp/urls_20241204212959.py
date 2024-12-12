from django.urls import path
from .views import register,CustomLoginView,profile_view,CustomLogoutView,update_user,view_participation,view_sponsorships
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/<str:pk>/', profile_view, name='profile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('update_user/<str:pk>/', update_user, name='update_user'),
    path('participationList/<str:pk>/', view_participation, name='participationList'),
    
    path('sponsorshipList/<str:pk>/', view_sponsorships, name='sponsorshipList'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='userApp/forgot_password.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='userApp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='userApp/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='userApp/password_reset_complete.html'), name='password_reset_complete'),

        path('video/', views.face_recognition_video, name='face_recognition_video'),

]
