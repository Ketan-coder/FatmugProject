from django.apps import AppConfig


class MainappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Mainapp"

    def ready(self):
        import Mainapp.signals
