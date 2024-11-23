from django.core.mail import send_mail
from django.contrib.auth import get_user_model

def on_new_tournament_equipment(sender, instance, created, **kwargs):
    if created:  # Checks if the object is newly created
        print(f"New TournamentEquipment added: {instance}")

        # Get all users with role = TournamentAdmin
        User = get_user_model()
        tournament_admins = User.objects.filter(role="TournamentAdmin")

        # Send email to all TournamentAdmins
        subject = "New Tournament Equipment Added"
        message = f"A new tournament equipment has been added:\n\nDetails:\n{instance}"
        from_email = "noreply@yourdomain.com"
        recipient_list = [admin.email for admin in tournament_admins if admin.email]

        if recipient_list:
            send_mail(
                subject,
                message,
                from_email,
                recipient_list,
                fail_silently=False,  # Raise an error if email fails
            )
