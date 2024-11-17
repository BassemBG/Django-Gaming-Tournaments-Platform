from django.shortcuts import render, redirect
from .models import participation  
from TournamentApp.models import tournament  
from userApp.models import user  as User
from django.contrib import messages
from django.views.generic import DeleteView
from django.urls import reverse_lazy

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        cin = request.POST.get('user')
        tournament_id = request.POST.get('tournament')  # Get the tournament ID
        team_name = request.POST.get('team_name')

        # Retrieve the tournament instance
        Tournament = get_object_or_404(tournament, id=tournament_id)
        Userr = get_object_or_404(User, cin=cin)

        # Create a new participation instance
        new_participation = participation(
            participant=Userr,
            tournament=Tournament   ,  # Assign the tournament instance
            team_name=team_name
        )
        new_participation.full_clean()  # Validate the model
        new_participation.save()
        
        messages.success(request, 'Registration successful! You can now log in.')

        return redirect('profile', pk=cin)


from django.urls import reverse
from django.views.generic import DeleteView
from .models import participation  # Ensure you import your participation model

class ParticipationDeleteView(DeleteView):
    model = participation
    template_name = 'Participation/participation_confirm_delete.html'
    
    def get_success_url(self):
        # Get the instance of the participation being deleted
        participation_instance = self.object
        # Access the related participant (User) instance
        user = participation_instance.participant
        
        # Build the URL to redirect to the user's profile
        return reverse('participationList', kwargs={'pk': user.cin})  # Use 'pk' or the appropriate parameter name
