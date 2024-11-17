from django.views.generic import CreateView
from django.contrib.auth.views import LoginView 
from django.urls import reverse_lazy
from .models import Participant
from .form import ParticipantCreationForm  

class UserCreateView(CreateView):
    model = Participant
    form_class = ParticipantCreationForm
    template_name = 'userApp/register.html'
    success_url = reverse_lazy('login')  
    
class CustomLoginView(LoginView):
    template_name = 'userApp/login.html'
    def get_success_url(self):
        return reverse_lazy('admin:index')

