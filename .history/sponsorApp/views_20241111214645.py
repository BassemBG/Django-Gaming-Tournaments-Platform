from django.shortcuts import render, redirect
from .models import sponsor 

def Sponsors_list(request):
    sponsors = sponsor.objects.all()  
    tournament =
    return render(request, 'coreApp/sponsors.html', {'sponsors': sponsors}) 
