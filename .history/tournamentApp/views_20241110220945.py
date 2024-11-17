from django.shortcuts import render
from gamesman.models import Game
from TournamentApp.models import tournament
from sponsorApp.models import sponsor

def home(request):
    tournaments = tournament.objects.all()
    return render(request, 'coreApp/index.html', {'tournaments': tournaments})  # Pass games to the index template
# Create your views here.
