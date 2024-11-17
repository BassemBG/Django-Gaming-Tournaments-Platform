from django.shortcuts import render, redirect
from .models import Game 
#from .forms import SuggestedGameForm
"""
def game_list(request):
    games = Game.objects.all()  # Fetch all game records
    suggestion_form = SuggestedGameForm()  # Initialize the suggestion form

    if request.method == 'POST':
        suggestion_form = SuggestedGameForm(request.POST)
        if suggestion_form.is_valid():
            suggestion_form.save()  # Save the suggestion to the SuggestedGame model
            return redirect('game_list')  # Redirect back to the game list

    return render(request, 'gamesman/game_list.html', {'games': games, 'form': suggestion_form})"""
"""
def suggest_game(request):
    if request.method == 'POST':
        form = SuggestedGameForm(request.POST)
        if form.is_valid():
            form.save()  # Save to SuggestedGame model
            return redirect('game_list')
    else:
        form = SuggestedGameForm()

    return render(request, 'gamesman/suggest_game.html', {'form': form})"""

def index(request):
    games = Game.objects.all()  # Fetch all game records
    return render(request, 'gamesman/index.html', {'games': games})  # Pass games to the index template
