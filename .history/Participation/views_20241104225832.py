from django.shortcuts import render
from .models import participation


def register(request):
    if request.method == 'POST':
        user = request.POST['user']
        tournament = request.POST['tournament']
        team_name = request.POST['team_name']
        try:
            new_participation = participation(
                username=username,
                cin = cin,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password),  
                role=role,
                is_staff=True if role == 'admin' else False
            )
            new_user.save()  
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  

        except ValidationError as e:
            messages.error(request, f"Error: {e.messages}")  
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")  

    return render(request, 'userApp/register.html')