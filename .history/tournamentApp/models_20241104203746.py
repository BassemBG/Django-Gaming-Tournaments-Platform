from django.db import models
from gamesman.models import Game

class tournament(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ('upcoming', 'Upcoming'),
            ('ongoing', 'Ongoing'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled')
        ]
    )
    prize = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    team_size = models.IntegerField()
    game = models.ForeignKey(game, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name