from celery import Celery
from social_n.celery import app

from .models import EventModel, Event
from django.contrib.contenttypes.models import ContentType


@app.task(bind=True)
def debug_task(self, instance_id, content_type_id, author):
    print("AZAZAZ")
    content = ContentType.objects.get_for_id(content_type_id)

    e = Event()
    e.content_type = content
    e.object_id = instance_id
    e.user_to_show_id = author
    e.save()