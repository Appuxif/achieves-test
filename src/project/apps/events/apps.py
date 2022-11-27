from django.apps import AppConfig


class EventsConfig(AppConfig):
    """Events"""

    name = "project.apps.events"

    def ready(self):
        import project.apps.events.signals
