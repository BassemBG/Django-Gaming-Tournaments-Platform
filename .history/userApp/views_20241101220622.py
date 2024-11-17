import logging
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password  # Import for password hashing
from .models import Participant  # Ensure to import your User model

def home(request):
    return render(request, 'users/register.html')

class login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)  
            return redirect('home')  
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'users/login.html')  


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        role = request.POST.get('role', 'player')  # Default to 'player' if not provided

        try:
            new_user = Participant(
                username=username,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password),  
                role=role
            )
            new_user.save()  
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login_user')  

        except ValidationError as e:
            messages.error(request, f"Error: {e.messages}")  
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")  

    return render(request, 'users/register.html')  
