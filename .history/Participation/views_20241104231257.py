from django.shortcuts import render, redirect
from .models import participation  # Make sure the model name is correctly capitalized
from django.contrib import messages
from django.core.exceptions import ValidationError

def register(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        tournament = request.POST.get('tournament')
        team_name = request.POST.get('team_name')
        new_participation = participation(
            user=user,
            tournament=tournament,
            team_name=team_name
        )
        new_participation.full_clean()  # Validate before saving
        new_participation.save()
        messages.success(request, 'Registration successful! You can now log in.')
            

      
    # For GET requests, you can render a registration form or redirect
    return render(request, 'registration_form.html')  # Adjust the template name as needed
