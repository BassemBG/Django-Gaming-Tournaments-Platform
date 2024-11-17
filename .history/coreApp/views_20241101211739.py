from django.shortcuts import render

def home(request):
    return render(request, 'coreApp/index.html')
# Create your views here.
