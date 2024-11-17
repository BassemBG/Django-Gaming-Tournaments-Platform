from django.shortcuts import render, redirect
from .models import sponsor 

def Games_list(request):
    games = sponsor.objects.all()  
    return render(request, 'coreApp/fighter.html', {'games': games}) 
