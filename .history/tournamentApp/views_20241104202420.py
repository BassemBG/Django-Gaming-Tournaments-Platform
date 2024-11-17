from django.shortcuts import render


def get(self, request):
    return render(request, 'tournament.html')
