from django.contrib.auth.views import LoginView , LogoutView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect,reverse
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import user
from django.views.generic import DetailView
from TournamentApp.models import tournament

class UserDetailView(DetailView):
    model = user
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
            new_user = user(
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
                return reverse('profile', kwargs={'pk': self.request.user.pk})
            return reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context['tournaments'] = Tournament.objects.all()
        return context

            CustomLoginView.get_context_data = get_context_data
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')
    
class updateProfile(DetailView):
    model = user
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