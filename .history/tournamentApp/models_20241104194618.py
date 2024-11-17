# Create your models here.
from django.db import models
from sponsorApp.models import Sponsor
from equipmentApp.models import Equipment
#import equipment
#importing member model

# Create your models here.
class TournamentStatus(models.TextChoices):
    UPCOMING = 'upcoming', 'Upcoming'
    ACTIVE = 'active', 'Active'
    FINISHED = 'finished', 'Finished'
    CANCELLED = 'cancelled', 'Cancelled'
    POSTPONED = 'postponed', 'Postponed'

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    requirements = models.TextField()
    tournament_status = models.CharField(
        max_length=10,
        choices=TournamentStatus.choices,
        default=TournamentStatus.UPCOMING
    )
    price = models.IntegerField()
    prize = models.CharField(max_length=100)
    team_size = models.IntegerField()
    location = models.CharField(max_length=100)

    # Timestamp fields:
    created_at = models.DateTimeField(auto_now_add=True)  # Set once on creation
    updated_at = models.DateTimeField(auto_now=True)      # Update every time the record is saved
    #Foreign fields:
    sponsors = models.ManyToManyField(Sponsor,through='Sponsorship', related_name="tournaments")
    equipments = models.ManyToManyField(Equipment,through='AssignEquipment', related_name='tournaments')
    #game = models.ForeignKey(Game,on_delete=models.CASCADE, related_name="tournaments")

    def show_tournament(self):
        return f"{self.name} - {self.tournament_status}"

    def _str_(self):
        return self.name

class ParticipationStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    CONFIRMED = 'confirmed', 'Confirmed'
    CANCELLED = 'cancelled', 'Cancelled'
    COMPLETED = 'completed', 'Completed'

class Participation(models.Model):
    status = models.CharField(
        max_length=10,
        choices=ParticipationStatus.choices,
        default=ParticipationStatus.PENDING
    )
    entryFeePaid = models.BooleanField(default=False)
    score = models.IntegerField(default=0)
    feedback = models.TextField(null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    #Foreign Keys:
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name="participations")
    #member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="participations")

class AssignEquipment(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Tournament, on_delete=models.CASCADE)