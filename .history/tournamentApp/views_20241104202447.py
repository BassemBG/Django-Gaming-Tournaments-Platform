from django.shortcuts import render
from TournamentApp.models import tournament

def get(self, request):
    tournaments = tournament.objects.all()
    return render(request, 'tournament.html')
