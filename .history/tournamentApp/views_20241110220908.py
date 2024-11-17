from django.shortcuts import render
from gamesman.models import Game
from TournamentApp.models import tournament
from sponsorApp.models import sponsor

def home(request):
    games = Game.objects.all()  # Fetch all game records
    tournaments = tournament.objects.all()
    sponsors = sponsor.objects.all()
    return render(request, 'coreApp/index.html', {tournaments': tournaments, 'sponsors': sponsors})  # Pass games to the index template
# Create your views here.
