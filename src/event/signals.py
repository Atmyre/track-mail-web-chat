from django.db.models.signals import post_save

from .models import EventModel, Event


def create_event(instance):
    e = Event()
    e.user_to_show = instance.get_author()
    e.title = instance.get_title()
    e.published = True
    #e.content_object = instance


for model in EventModel.__subclasses__:
    post_save.connect(create_event, model)