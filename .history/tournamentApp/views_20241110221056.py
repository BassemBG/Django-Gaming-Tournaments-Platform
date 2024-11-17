from django.shortcuts import render
from TournamentApp.models import tournament

def T(request):
    tournaments = tournament.objects.all()
    return render(request, 'TournamentApp/elements.html', {'tournaments': tournaments}) 
