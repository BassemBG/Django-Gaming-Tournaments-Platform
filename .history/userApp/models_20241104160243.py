# In Participant/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class Participant(AbstractUser):
    cin_validator = RegexValidator(
        regex=r'^\d{8}$',
        message="This field must contain exactly 8 digits"
    )
    cin = models.CharField(primary_key=True, max_length=8, validators=[cin_validator])
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    username = models.CharField(unique=True, max_length=255)
    USERNAME_FIELD = 'username'
    CHOIX = (
        ('Player', 'Player'),
        ('Admin', 'Admin'),
    )
    participant_category = models.CharField('participant_category', choices=CHOIX, max_length=255)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='participant_set',
        blank=True,
        help_text="The groups this user belongs to."
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='participant_set',
        blank=True,
        help_text="Specific permissions for this user."
    )

    
 

    def clean(self):
        # Additional validation logic if needed
        pass
    class Meta:
        verbose_name_plural = 'Participants'

