from django.shortcuts import render
from gamesman.models import Game
from TournamentApp.models import tournament
from spo.models import tournament

def home(request):
    games = Game.objects.all()  # Fetch all game records
    tournaments = tournament.objects.all()
    return render(request, 'coreApp/index.html', {'games': games, 'tournaments': tournaments})
# Create your views here.
