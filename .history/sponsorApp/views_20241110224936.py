from django.shortcuts import render, redirect
from .models import sponsor 

def Sponsors_list(request):
    sponsors = sponsor.objects.all()  
    return render(request, 'coreApp/sponsors.html', {'sponsors': sponsors}) 
