from django.shortcuts import render
from TournamentApp.models import tournament

def tournamentsList(self, request): 
    
    return render(request, 'coreApp/index.html', {'tournaments': tournaments})
