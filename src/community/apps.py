from __future__ import unicode_literals

from django.apps import AppConfig


class CommunityConfig(AppConfig):
    name = 'community'
    def ready(self):
        import signals
