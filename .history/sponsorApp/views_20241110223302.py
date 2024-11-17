from django.shortcuts import render, redirect
from .models import sponsor 

def sponsors(request):
    sponsors = sponsor.objects.all()  
    return render(request, 'coreApp/blog.html', {'sponsors': sponsors}) 
