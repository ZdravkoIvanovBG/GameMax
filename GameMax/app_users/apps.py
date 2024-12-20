from django.apps import AppConfig


class AppUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GameMax.app_users'
    verbose_name = 'User Management'

    def ready(self):
        import GameMax.app_users.signals
