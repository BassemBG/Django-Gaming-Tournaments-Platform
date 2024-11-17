from django.db import models
from userApp.models import user
from TournamentApp.models import tournament

class participation(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    tournament = models.ForeignKey(tournament, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.team_name
