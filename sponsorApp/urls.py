from django.urls import path
from .views import Sponsors_form,register_sponsorship,registerSponsor


urlpatterns = [
    path('Sponsors_form', Sponsors_form, name='Sponsors_form'),
    path('register_sponsor', register_sponsorship, name='register_sponsor'),
    path('registerSponsor', registerSponsor, name='registerSponsor'),
]