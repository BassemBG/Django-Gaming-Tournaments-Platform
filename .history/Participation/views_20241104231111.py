from django.shortcuts import render, redirect
from .models import participation  # Make sure the model name is correctly capitalized
from django.contrib import messages
from django.core.exceptions import ValidationError

def register(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        tournament = request.POST.get('tournament')
        team_name = request.POST.get('team_name')
        
        try:
            new_participation = participation(  # Ensure the model is properly referenced
                user=user,
                tournament=tournament,
                team_name=team_name
            )
            new_participation.full_clean()  # Validate before saving
            new_participation.save()
            messages.success(request, 'Registration successful! You can now log in.')
            

        except ValidationError as e:
            messages.error(request, f"Error: {', '.join(e.messages)}")  
            return redirect('registration_page')  # Redirect back to registration page to fix errors
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
            return redirect('registration_page')  # Redirect back to registration page in case of a general error

    # For GET requests, you can render a registration form or redirect
    return render(request, 'registration_form.html')  # Adjust the template name as needed
