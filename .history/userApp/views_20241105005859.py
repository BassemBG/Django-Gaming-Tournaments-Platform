from django.contrib.auth.views import LoginView , LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect,reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import user as User
from django.views.generic import DetailView
from TournamentApp.models import tournament
from Participation.models import participation
from django.shortcuts import get_object_or_404

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
    
class updateProfile(DetailView):
    model = User
    template_name = 'userApp/profile_edit.html'
    context_object_name = 'user'
    ordering = ['username']
    
    def post(self, request, *args, **kwargs):
        user = user.objects.get(pk=self.kwargs['pk'])
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        return redirect('profile', pk=user.pk)    


def profile_view(request, pk):
    user = get_object_or_404(User, pk=pk)
    tournaments = tournament.objects.all()
    participations = participation.objects.filter(participant=user)
    return render(request, 'userApp/profile.html', {'user': user, 'tournaments': tournaments,'participations':participations})  # Pass games to the index template


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import User  # Adjust the import based on your user model

@login_required  # Ensure the user is logged in
def update_user(request):
    user = get_object_or_404(User, id=request.user.id)  # Get the currently logged-in user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')  # Changed from 'phone' to 'username'
        user.save()  # Save the updated user information
        return redirect('profile', pk=user.id)  # Redirect to the user's profile or desired page

    # If the request method is GET, render the form with the current user data
    return render(request, 'your_template.html', {'user': user})  # Replace 'your_template.html' with your actual template name
    