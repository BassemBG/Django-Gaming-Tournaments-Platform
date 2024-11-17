from django.urls import path
from .views import login_view

urlpatterns = [
    path('register/', login_view, name='home'),
    path('login/', home, name='home'),
]