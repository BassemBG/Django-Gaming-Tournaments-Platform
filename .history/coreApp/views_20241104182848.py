from django.shortcuts import render
from ga

def home(request):
    games = Game.objects.all()  # Fetch all game records
    return render(request, 'gamesman/index.html', {'games': games})
# Create your views here.
