from django.db import models
from sponsorApp.models import sponsor
from TournamentApp.models import tournament

class sponsorship(models.Model):
    sponsor = models.ForeignKey(sponsor, on_delete=models.CASCADE)
    tournament = models.ForeignKey(tournament, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
            ('terminated', 'Terminated')
        ]
    )
    
    def __str__(self):
        return self.sponsor.name + ' - ' + self.tournament.name
    
    def clean(self):
        rif 

# Create your models here.
