from django.shortcuts import render
from TournamentApp.models import tournament,TournamentEquipment

def Tournaments_View(request):
    tournaments = tournament.objects.all()
    return render(request, 'coreApp/tournaments.html', {'tournaments': tournaments}) 
def completed_tournaments_view(request):
    # Step 1: Get completed tournaments
    completed_tournaments = tournament.objects.filter(status='completed')
    print(f"Completed Tournaments: {completed_tournaments}")
    
    # Step 2: Get associated equipment for completed tournaments
    completed_tournament_equipment = TournamentEquipment.objects.filter(tournament__in=completed_tournaments)
    print(f"Completed Tournament Equipment: {completed_tournament_equipment}")

    # Step 3: Pass the filtered equipment to the template
    return render(request, 'coreApp/completed_tournaments.html', {'completed_tournament_equipment': completed_tournament_equipment})