from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Configuration for the checkout app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'checkout'

    def ready(self):
        """
        Method called when the app is ready.
        Import signals module to ensure signal handlers are registered.
        """
        import checkout.signals

