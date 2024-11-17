from django.db import models
from userApp.models import user
from TournamentApp.models import tournament

class participation(models.Model):
    participant = models.ForeignKey(user, on_delete=models.CASCADE)
    tournament = models.ForeignKey(tournament, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)
    def __str__(self):
        return self.team_name
    class Meta:
        unique_together = ('participant', 'tournament')
        
class Payment(models.Model):
    participation = models.ForeignKey(participation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_payment_intent_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default="pending")
