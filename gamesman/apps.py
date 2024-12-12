from django.apps import AppConfig


class GamesmanConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gamesman'
    def ready(self):
        import gamesman.signals
