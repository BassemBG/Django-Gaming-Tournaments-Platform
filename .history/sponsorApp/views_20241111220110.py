from django.shortcuts import render, redirect
from .models import sponsor 
from TournamentApp.models import tournament
from django.http import HttpResponse
from .forms import SponsorForm

def Sponsors_list(request):
    sponsors = sponsor.objects.all()  
    tournaments = tournament.objects.all()
    return render(request, 'coreApp/sponsors.html', {'sponsors': sponsors,'tournaments':tournaments}) 

def register_sponsor(request):
    if request.method == 'post':
        form = SponsorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sponsors_list')
        else:
            form = SponsorForm()
    sponsors = sponsor.objects.all()
    tournaments = tournament.objects.all()
    return render(request, 'coreApp/register_sponsor.html', {'form': form, 'sponsors': sponsors, 'tournaments': tournaments})