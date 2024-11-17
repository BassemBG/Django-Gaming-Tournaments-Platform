from django.db import models
from userApp.models import user
from TournamentApp.models import tournament

class participation(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    tournament = models.ForeignKey(tournament, on_delete=models.CASCADE)
    team_name = models.CharField(max_length=100)
    team_size = models.IntegerField()
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.team_name
