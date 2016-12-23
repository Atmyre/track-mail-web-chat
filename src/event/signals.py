from django.db.models.signals import post_save
from django.utils.cache import caches
from .models import EventModel, Event
from .tasks import debug_task
from django.contrib.contenttypes.models import ContentType


cache = caches['default']


def create_event(sender, **kwargs):
    print(sender)
    debug_task.apply_async(args=[kwargs.get('instance').id, ContentType.objects.get_for_model(sender).id, kwargs.get('instance').author.id ])


def event_post_save(instance, created=False, **kwargs):
    if created:
        cache.set(instance.get_descr_cache_key(), None)


def init_signals():
    for model in EventModel.__subclasses__():
        post_save.connect(create_event, sender=model)
        post_save.connect(event_post_save, Event)


