from django.db.models.signals import post_save

from .models import EventModel, Event
from .tasks import debug_task
from django.contrib.contenttypes.models import ContentType


def create_event(sender, **kwargs):
    print(sender)
    debug_task.apply_async(args=[kwargs.get('instance').id, ContentType.objects.get_for_model(sender).id, kwargs.get('instance').author.id ])


def init_signals():
    for model in EventModel.__subclasses__():
        post_save.connect(create_event, sender=model)