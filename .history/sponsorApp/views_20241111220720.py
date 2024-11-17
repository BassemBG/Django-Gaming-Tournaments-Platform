from django.shortcuts import render, redirect
from .models import sponsor 
from TournamentApp.models import tournament
from django.http import HttpResponse
from .forms import SponsorshipForm
from django.contrib import messages


def Sponsors_list(request):
    sponsors = sponsor.objects.all()  
    tournaments = tournament.objects.all()
    return render(request, 'coreApp/sponsors.html', {'sponsors': sponsors,'tournaments':tournaments}) 

