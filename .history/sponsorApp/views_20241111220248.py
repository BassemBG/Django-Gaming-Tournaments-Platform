from django.shortcuts import render, redirect
from .models import sponsor 
from TournamentApp.models import tournament
from django.http import HttpResponse
import m

def Sponsors_list(request):
    sponsors = sponsor.objects.all()  
    tournaments = tournament.objects.all()
    return render(request, 'coreApp/sponsors.html', {'sponsors': sponsors,'tournaments':tournaments}) 

def register_sponsor(request):
    if request.method == 'POST':
        form = SponsorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Sponsor registration successful!')
            return redirect('sponsors_list')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SponsorForm()

    tournaments = tournament.objects.all()
    return render(request, 'userApp/register.html', {'form': form, 'tournaments': tournaments})
