from django.db import models
from django.core.exceptions import ValidationError
from gamesman.models import Game
from equipmentApp.models import Equipment
from django.utils import timezone

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
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name
class TournamentEquipment(models.Model):
    tournament = models.ForeignKey(tournament, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, help_text="Quantity of this equipment for the tournament")

    def __str__(self):
        return f"{self.equipment.name} for {self.tournament.name}"

    def clean(self):
        """Custom validation to ensure the requested quantity does not exceed available stock."""

        # Calculate total reserved quantity for ongoing tournaments
        ongoing_reservations = TournamentEquipment.objects.filter(
            equipment=self.equipment,
            tournament__status='ongoing'
        ).exclude(id=self.id)

        # Sum up quantities already reserved for this equipment in other ongoing tournaments
        reserved_quantity = sum(item.quantity for item in ongoing_reservations)
        
        # Calculate remaining available stock
        available_stock = self.equipment.stock_quantity - reserved_quantity
        
        # Check if the requested quantity exceeds available stock
        if self.quantity > available_stock:
            raise ValidationError(
                f"Insufficient stock for '{self.equipment.name}'. Available: {available_stock}, requested: {self.quantity}."
            )

    def save(self, *args, **kwargs):
        # Run the clean method to apply custom validation
        self.clean()
        super().save(*args, **kwargs)