from django.shortcuts import render, redirect
from .models import sponsor 
from TournamentApp.models import tournament

def Sponsors_list(request):
    sponsors = sponsor.objects.all()  
    tournament = tournament.objects
    return render(request, 'coreApp/sponsors.html', {'sponsors': sponsors}) 
