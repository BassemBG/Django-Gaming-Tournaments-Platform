# In Participant/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from Conference.models import conference  # Import Conference model directly

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

    USERNAME_FIELD = 'username'

    CHOIX = (
        ('ETUDIANT', 'ETUDIANT'),
        ('CHERCHEUR', 'CHERCHEUR'),
        ('ENSEIGNANT', 'ENSEIGNANT'),
        ('DOCTEUR', 'DOCTEUR'),
    )
    participant_category = models.CharField('participant_category', choices=CHOIX, max_length=255)

    # Change this to reference Reservation model instead
    reservations = models.ManyToManyField('Reservation', related_name='participants', blank=True)

    def clean(self):
        # Additional validation logic if needed
        pass
    class Meta:
        verbose_name_plural = 'Participants'


class Reservation(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    conference = models.ForeignKey(conference, on_delete=models.CASCADE)
    reservation_date = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Reservations'
        unique_together = ('conference', 'participant')
