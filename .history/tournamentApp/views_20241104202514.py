from django.shortcuts import render
from TournamentApp.models import tournament

def tournamentsList(self, request):
    tournaments = tournament.objects.all()
    return render(request, 'index.html', {'tournaments': tournaments})
