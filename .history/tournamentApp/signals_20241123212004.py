from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TournamentEquipment  # Replace with your model's import
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings  # For accessing DEFAULT_FROM_EMAIL


@receiver(post_save, sender=TournamentEquipment)
def on_new_tournament_equipment(sender, instance, created, **kwargs):
    if created:  # Checks if the object is newly created
        print(f"New TournamentEquipment added: {instance}")
        # Place your custom action here
        # For example:
        # send_notification(instance)
        # log_event(instance)



def on_new_tournament_equipment(sender, instance, created, **kwargs):
    