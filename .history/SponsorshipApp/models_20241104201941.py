from django.db import models
from sponsorApp.models import sponsor
from TournamentApp.models import tournament

class sponsorship(models.Model):
    sponsor = models.ForeignKey(sponsor, on_delete=models.CASCADE)
    tournament = models.ForeignKey(tournament, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    status = 
    
    def __str__(self):
        return self.sponsor.name + ' - ' + self.tournament.name

# Create your models here.
