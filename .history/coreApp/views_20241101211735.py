from django.shortcuts import render

def home(request):
    return render(request, 'coreApp.html')
# Create your views here.
