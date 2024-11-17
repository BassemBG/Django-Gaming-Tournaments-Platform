from django.shortcuts import render, redirect
from .models import participation  
from .models import Tournament  
from django.contrib import messages
from django.core.exceptions import ValidationError

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        tournament_id = request.POST.get('tournament')  # Get the tournament ID
        team_name = request.POST.get('team_name')

        # Retrieve the tournament instance
        tournament = get_object_or_404(Tournament, id=tournament_id)

        # Create a new participation instance
        new_participation = participation(
            user=user,
            tournament=tournament,  # Assign the tournament instance
            team_name=team_name
        )
        new_participation.full_clean()  # Validate the model
        new_participation.save()
        
        messages.success(request, 'Registration successful! You can now log in.')

        # Return a JSON response to trigger a page reload
        return JsonResponse({'status': 'success'})

    # For GET requests, render the registration form
    return render(request, 'registration_form.html')  # Adjust template as needed
