from django.db import models
from userApp.models import user
from TournamentApp.models import tournament

class participation(models.Model):
    participant = models.ForeignKey(user, on_delete=models.CASCADE)
    tournament = models.ForeignKey(tournament, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)
    def __str__(self):
        return self.team_name
    