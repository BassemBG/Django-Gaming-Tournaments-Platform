from django.shortcuts import render, redirect
from .models import sponsor 
import TournamentApp

def Sponsors_list(request):
    sponsors = sponsor.objects.all()  
    tournament = 
    return render(request, 'coreApp/sponsors.html', {'sponsors': sponsors}) 
