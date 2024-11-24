from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TournamentEquipment
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model
from django.conf import settings


@receiver(post_save, sender=TournamentEquipment)
def on_new_tournament_equipment(sender, instance, created, **kwargs):
    if created:  # Execute only when a new TournamentEquipment is added
        print(f"New TournamentEquipment added: {instance}")

        # Get all users with role = TournamentAdmin
        User = get_user_model()
        tournament_admins = User.objects.filter(role="TournamentAdmin")

        # Extract tournament and equipment details
        tournament_name = instance.tournament.name
        equipment_name = instance.equipment.name
        equipment_quantity = instance.quantity
        stock_remaining = instance.equipment.stock_quantity

        # Email subject and recipients
        subject = "🏅 New Equipment Added to a Tournament"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [admin.email for admin in tournament_admins if admin.email]

        # Plain-text fallback message
        text_message = (
            f"{equipment_quantity} equipment(s) ({equipment_name}) have been added to the '{tournament_name}' tournament.\n\n"
            f"Remaining stock: {stock_remaining} equipment(s).\n"
            f"If you have a tournament during the same period as '{tournament_name}', please take note."
        )

        # HTML message
        html_message = f"""
        <html>
            <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
                <h2 style="color: #4CAF50;">🎉 New Equipment Added!</h2>
                <p><strong>{equipment_quantity}</strong> equipment(s) <em>({equipment_name})</em> have been added to the tournament:</p>
                <h3 style="color: #007BFF;">{tournament_name}</h3>
                <p><strong>Remaining stock:</strong> {stock_remaining} equipment(s).</p>
                <hr style="border: none; border-top: 1px solid #ccc;">
                <p style="color: #555;">⚠️ Please take note if you have a tournament scheduled during the same period as 
                <strong>{tournament_name}</strong>.</p>
                <p style="color: #999; font-size: 0.9em;">This is an automated notification from the GAME MASTER LEAGUE.</p>
            </body>
        </html>
        """

        # Send the email
        if recipient_list:
            try:
                email = EmailMultiAlternatives(
                    subject=subject,
                    body=text_message,
                    from_email=from_email,
                    to=recipient_list,
                )
                email.attach_alternative(html_message, "text/html")
                email.send()
                print("Beautiful email sent successfully")
            except Exception as e:
                print(f"Failed to send email: {e}")
