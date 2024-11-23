from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TournamentEquipment  # Replace with your model's import

@receiver(post_save, sender=TournamentEquipment)
def on_new_tournament_equipment(sender, instance, created, **kwargs):
    if created:  # Checks if the object is newly created
        print(f"New TournamentEquipment added: {instance}")
        # Place your custom action here
        # For example:
        # send_notification(instance)
        # log_event(instance)


from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings  # For accessing DEFAULT_FROM_EMAIL

def on_new_tournament_equipment(sender, instance, created, **kwargs):
    if created:  # Checks if the object is newly created
        print(f"New TournamentEquipment added: {instance}")

        # Get all users with role = TournamentAdmin
        User = get_user_model()
        tournament_admins = User.objects.filter(role="TournamentAdmin")

        # Send email to all TournamentAdmins
        subject = "New Tournament Equipment Added"
        message = f"A new tournament equipment has been added:\n\nDetails:\n{instance}"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [admin.email for admin in tournament_admins if admin.email]

        if recipient_list:
            try:
                send_mail(
                    subject,
                    message,
                    from_email,
                    recipient_list,
                    fail_silently=False,  # Raise an error if email fails
                )
                print("Email sent successfully")
            except Exception as e:
                print(f"Failed to send email: {e}")
