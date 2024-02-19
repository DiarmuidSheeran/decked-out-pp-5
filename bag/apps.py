from django.apps import AppConfig


class BagConfig(AppConfig):
    """
    AppConfig class for the Bag app.

    This class defines configuration settings for the Bag app,
    including the default auto field and the name of the app.

    Attributes:
        default_auto_field (str): The default auto field for models.
        name (str): The name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'

