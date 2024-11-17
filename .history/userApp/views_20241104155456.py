from django.contrib.auth.views import LoginView , LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect,reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import Participant
from django.views.generic import DetailView

class UserDetailView(DetailView):
    model = Participant
    template_name = 'userApp/profile.html'
    context_object_name = 'participant'
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
            new_user = Participant(
                username=username,
                cin = cin,
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password),  
                participant_category=role,
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
        if self.request.user.participant_category == 'Admin':
            return reverse_lazy('admin:index')
        # Use the actual instance of the user
        cin = self.request.user.pk
        if self.request.user.is_authenticated and cin:
            return reverse('profile', kwargs={'pk': self.request.user.pk})
        return reverse_lazy('home')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    
class u    