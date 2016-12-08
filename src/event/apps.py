from __future__ import unicode_literals

from django.apps import AppConfig


class EventConfig(AppConfig):
    name = 'event'

    def ready(self):
        from .signals import init_signals
        init_signals()

