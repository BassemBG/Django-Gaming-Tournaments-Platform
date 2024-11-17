from django.shortcuts import render
from TournamentApp.models import tournament

def Tournaments_View(request):
    tournaments = tournament.objects.all()
    return render(request, 'coreApp/elements.html', {'tournaments': tournaments}) 
