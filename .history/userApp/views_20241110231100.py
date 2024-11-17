from django.contrib.auth.views import LoginView , LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect,reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import user as User
from django.views.generic import DetailView, UpdateView
from TournamentApp.models import tournament
from Participation.models import participation
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class UserDetailView(DetailView):
    model = User
    template_name = 'userApp/profile.html'
    context_object_name = 'user'
    ordering = ['username']
    
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        role = request.POST.get('role', 'player')  # Default to 'player' if not provided
        cin = request.POST['cin']

        try:
            new_user = User(
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
    
class CustomLoginView(LoginView):
    template_name = 'userApp/login.html'
    def get_success_url(self):
        if self.request.user.is_staff:
            return reverse_lazy('admin:index')
        else:   
            cin = self.request.user.pk
            if self.request.user.is_authenticated and cin:
                return reverse('profile', kwargs={'pk': cin})
            return reverse_lazy('home')
    

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    
def update_user(request, user_id):
    user = get_object_or_404(User, cin=user_id)  # Get the user instance
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.save()  # Save the updated user information
        return redirect('    <style>
        /* Custom CSS to style the login form */
        .banner_part {
            display: flex;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            background-color: #f8f9fa;
        }
        .login-form-container {
            max-width: 400px;
            width: 100%;
            padding: 20px;
            background: rgba(232, 231, 231, 0.7); /* Darker transparent background */
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .login-form-container h1 {
            margin-bottom: 20px;
            font-size: 24px;
            color: #fff; /* White text color for contrast */
        }
        .login-form-container .form-group {
            margin-bottom: 15px;
        }
        .login-form-container input[type="text"],
        .login-form-container input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }
        .login-form-container input[type="submit"] {
            width: 100%;
            padding: 10px;
            margin-top: 15px;
            border-radius: 5px;
            border: none;
            background-color: #ff0000; /* Red background for the button */
            color: white;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .login-form-container input[type="submit"]:hover {
            background-color: #cc0000;
        }
        .login-form-container .dont-have-account {
            margin-top: 15px;
            font-size: 14px;
            color: #fff; /* White text color for contrast */
        }
        .login-form-container .dont-have-account a {
            color: #007bff;
            text-decoration: none;
        }
    </style>', pk=user_id)  # Redirect to the user's profile or desired page
    return redirect('profile', pk=user_id)


@login_required    
def profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    tournaments = tournament.objects.all()
    participations = participation.objects.filter(participant=user)
    return render(request, 'userApp/profile.html', {'user': user, 'tournaments': tournaments,'participations':participations})  # Pass games to the index template

