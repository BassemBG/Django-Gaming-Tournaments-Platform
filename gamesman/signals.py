from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Game
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model
from django.conf import settings


@receiver(post_save, sender=Game)
def on_new_game(sender, instance, created, **kwargs):
    if created:  # Execute only when a new Game is added
        print(f"New game added: {instance}")

        # Get all users with role = GamesAdmin
        User = get_user_model()
        games_admins = User.objects.filter(role="GamesAdmin")

        # Extract game details
        game_title = instance.Game_Title
        genre = instance.Genre
        platform = instance.Platform
        release_date = instance.Release_Date
        developer = instance.Developer
        publisher = instance.Publisher
        nb_players = instance.Nb_Players
        file_size = instance.File_Size

        # Email subject and recipients
        subject = "🎮 New Game Added to the Platform"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [admin.email for admin in games_admins if admin.email]

        # Plain-text fallback message
        text_message = (
            f"A new game has been added to the platform:\n\n"
            f"Title: {game_title}\n"
            f"Genre: {genre}\n"
            f"Platform: {platform}\n"
            f"Release Date: {release_date}\n"
            f"Developer: {developer}\n"
            f"Publisher: {publisher}\n"
            f"Number of Players: {nb_players}\n"
            f"File Size: {file_size}\n"
        )

        # HTML message
        html_message = f"""
        <html>
            <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
                <h2 style="color: #4CAF50;">🎉 New Game Added!</h2>
                <p>A new game has been added to the platform:</p>
                <ul>
                    <li><strong>Title:</strong> {game_title}</li>
                    <li><strong>Genre:</strong> {genre}</li>
                    <li><strong>Platform:</strong> {platform}</li>
                    <li><strong>Release Date:</strong> {release_date}</li>
                    <li><strong>Developer:</strong> {developer}</li>
                    <li><strong>Publisher:</strong> {publisher}</li>
                    <li><strong>Number of Players:</strong> {nb_players}</li>
                    <li><strong>File Size:</strong> {file_size}</li>
                </ul>
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
