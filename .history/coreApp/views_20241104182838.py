from django.shortcuts import render

def home(request):
    games = Game.objects.all()  # Fetch all game records
    return render(request, 'gamesman/index.html', {'games': games}) 
    return render(request, 'coreApp/index.html')
# Create your views here.
