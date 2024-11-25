from django.urls import path
from . import views
from userApp.views import view_sponsorships

urlpatterns = [
    #path('sponsorship-form/', views.sponsorship_form_view, name='sponsorship_form'),
    # Preselected tournament
    path('sponsorship_form/<int:tournament_id>/', views.sponsorship_form_view, name='sponsorship_form_preselected'),

    # General form with selectable tournament
    path('sponsorship_form/', views.sponsorship_form_view, name='sponsorship_form'),
    path('sponsorship_list/', view_sponsorships, name='sponsorship_list'),

]
