from django.shortcuts import render, redirect
from .models import sponsor 
from Spo.models import sponsor 
from TournamentApp.models import tournament
from django.http import HttpResponse
from .forms import RegisterSponsorForm
from django.contrib import messages


def Sponsors_list(request):
    sponsors = sponsor.objects.all()  
    tournaments = tournament.objects.all()
    return render(request, 'coreApp/sponsors.html', {'sponsors': sponsors,'tournaments':tournaments}) 

def register_sponsorship(request):
    if request.method == 'POST':
        form = RegisterSponsorForm(request.POST)
        if form.is_valid():
            # Automatically set the sponsor field to the current logged-in user
            form.instance.sponsor = request.user
            form.save()
            messages.success(request, 'Sponsor registration successful!')
            return redirect('sponsors_list')  # Redirect to the sponsors list page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegisterSponsorForm()