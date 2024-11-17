from django.db import models
from sponsorApp.models import sponsor
from TournamentApp.models import tournament
from django.core.exceptions import ValidationError
from django.utils import timezone

    def start_date_validator(value):
        if value < timezone.now().date():
            raise ValidationError('Start date must be in the future.')


class sponsorship(models.Model):

    sponsor = models.ForeignKey(sponsor, on_delete=models.CASCADE)
    start_date = models.DateField(validators=[start_date_validator])
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
        if self.start_date > self.end_date:
            raise ValidationError('Start date cannot be later than end date.') 

# Create your models here.
