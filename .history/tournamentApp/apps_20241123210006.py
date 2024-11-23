from django.apps import AppConfig


class TournamentappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TournamentApp'
    def ready(self):
        import your_app.signals