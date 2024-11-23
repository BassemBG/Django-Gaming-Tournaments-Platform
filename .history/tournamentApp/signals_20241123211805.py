from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings  # For accessing DEFAULT_FROM_EMAIL

def on_new_tournament_equipment(sender, instance, created, **kwargs):
    if created:  # Checks if the object is newly created
        print(f"New TournamentEquipment added: {instance}")
