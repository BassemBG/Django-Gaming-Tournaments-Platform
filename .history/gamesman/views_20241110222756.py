from django.shortcuts import render, redirect
from .models import Game 

def Games_list(request):
    games = Game.objects.all()  
    return render(request, 'coreApp/fighter.html', {'games': games}) 
