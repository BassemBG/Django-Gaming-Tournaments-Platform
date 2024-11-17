from django.urls import path
from .views import *

urlpatterns = [
    path('register_participation/', register, name='register_participation'),
    path('delete_participation/<int:pk>/', ParticipationDeleteView.as_view(), name='delete_participation'),
    path('payment/<int:tournament_id>/', process_payment, name='process_payment'),
    path('payment-success/<int:participation_id>/', payment_success, name='payment_success'),
]