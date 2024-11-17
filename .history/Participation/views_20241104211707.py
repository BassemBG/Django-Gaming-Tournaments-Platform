from django.shortcuts import render
from .models import participation


class ParticipationVCreate(CreateView):
    model = participation
    fields = ['user', 'tournament', 'team_name']
    template_name = 'Participation/participation_form.html'
    success_url = '/'
# Create your views here.
