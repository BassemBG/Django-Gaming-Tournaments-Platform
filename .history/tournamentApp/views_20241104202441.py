from django.shortcuts import render
from TournamentApp.models import tournament

def get(self, request):
    return render(request, 'tournament.html')
