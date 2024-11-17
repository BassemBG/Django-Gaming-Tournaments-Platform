from django.shortcuts import render
from .models import participation
from django.contrib import messages
from django.core.exceptions import ValidationError

def register(request):
    if request.method == 'POST':
        user = request.POST['user']
        tournament = request.POST['tournament']
        team_name = request.POST['team_name']
        try:
            new_participation = participation(
                user=user,
                tournament=tournament,
                team_name=team_name
            )
            new_participation.save()
            messages.success(request, 'Registration successful! You can now log in.')

        except ValidationError as e:
            messages.error(request, f"Error: {e.messages}")  
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")  

    return render(request, 'userApp/register.html')