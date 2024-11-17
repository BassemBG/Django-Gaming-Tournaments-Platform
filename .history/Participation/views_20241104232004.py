from django.shortcuts import render, redirect
from .models import participation  
from TournamentApp.models import tournament  
from userApp.models import user  as User
from django.contrib import messages
from django.core.exceptions import ValidationError

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        cin = request.POST.get('user')
        tournament_id = request.POST.get('tournament')  # Get the tournament ID
        team_name = request.POST.get('team_name')

        # Retrieve the tournament instance
        Tournament = get_object_or_404(tournament, id=tournament_id)
        Userr = get_object_or_404(User, cin=cin)

        # Create a new participation instance
        new_participation = participation(
            participant=Userr,
            tournament=Tournament   ,  # Assign the tournament instance
            team_name=team_name
        )
        new_participation.full_clean()  # Validate the model
        new_participation.save()
        
        messages.success(request, 'Registration successful! You can now log in.')
    
