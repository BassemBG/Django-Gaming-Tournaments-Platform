from django.shortcuts import render
from TournamentApp.models import tournament,TournamentEquipment

def Tournaments_View(request):
    tournaments = tournament.objects.all()
    return render(request, 'coreApp/tournaments.html', {'tournaments': tournaments}) 
