from __future__ import unicode_literals

from django.apps import AppConfig


class MessageConfig(AppConfig):
    name = 'message'

    def ready(self):
        from .signals import init_signals
        init_signals()
