from django.shortcuts import render

class tournamentView(Vie):
    def get(self, request):
        return render(request, 'tournament.html')
