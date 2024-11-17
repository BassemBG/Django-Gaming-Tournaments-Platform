from django.shortcuts import render, redirect
from .models import Game 

def Games(request):
    games = Game.objects.all()  # Fetch all game records
    return render(request, 'coreApp/index.html', {'games': games})  # Pass games to the index template
