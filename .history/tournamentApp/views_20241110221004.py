from django.shortcuts import render
from TournamentApp.models import tournament

def home(request):
    tournaments = tournament.objects.all()
    return render(request, 'TournamentApp/index.html', {'tournaments': tournaments}) 
