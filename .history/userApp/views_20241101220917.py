from django.views.generic import CreateView
from django.contrib.auth.views import LoginView 
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Participant,Reservation
from .form import ParticipantCreationForm  

class UserCreateView(CreateView):
    model = Participant
    form_class = ParticipantCreationForm
    template_name = 'userApp/register.html'
    success_url = reverse_lazy('login')  
    
class CustomLoginView(LoginView):
    template_name = 'userApp/login.html'
    def get_success_url(self):
        return reverse_lazy('conference_list')

class ReservationListView(ListView):
    model = Reservation
    template_name = 'Participant/reservation.html'
    context_object_name = "Reservations"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['categories'] = categorie.objects.all()
        
        #user_resevations = Reservation.objects.filter(user=self.request.user).values_list(conference_id, flat=True)
        #context['user_resevations'] = user_resevations
        
        return context
    def get_queryset(self):
        queryset= Reservation.objects.all().order_by('reservation_date')
        """id = self.request.GET.get('category')  
        if id:
            queryset = queryset.filter(category_id=id)"""
        return queryset
    
    from Participant.models import Participant
