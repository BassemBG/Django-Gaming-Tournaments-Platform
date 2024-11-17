from django.shortcuts import render
from .models import participation


class ParticipationView():
    def get(self, request):
        participations = participation.objects.all()
        return render(request, 'participation.html', {'participations': participations})
# Create your views here.
