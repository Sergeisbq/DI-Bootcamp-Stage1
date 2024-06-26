from django.apps import AppConfig


class ImageShareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image_share'

    def ready(self) -> None:
        import image_share.signals
