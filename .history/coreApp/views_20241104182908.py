from django.shortcuts import render
from gamesman.models import Game

def home(request):
    games = Game.objects.all()  # Fetch all game records
    return render(request, 'coreApp/index.html', {'games': games})
# Create your views here.
