from django.db import models

class Participant(AbstractUser):
    # Add additional fields here
    age = models.PositiveIntegerField(null=True, blank=True)
    
# Create your models here.
