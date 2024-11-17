from django.shortcuts import render, redirect
from .models import sponsor 

def Games_list(request):
    sponsors = sponsor.objects.all()  
    return render(request, 'coreApp/fighter.html', {'games': sponsors}) 
