from celery import Celery
from social_n.celery import app

from .models import Message
from django.contrib.contenttypes.models import ContentType
from login.models import UserProfile
from django.core.mail import send_mail


celery = Celery('tasks')
celery.config_from_object('celeryconfig')


@app.task(bind=True)
def send_lost_messages_notification(self):
    for user_profile in UserProfile.objects.filter():
        lost_message = user_profile.get_unread_messages()
        if lost_message == '':
            return
        send_mail("Messages you didn't get today", lost_message, 'atmyre@yandex.ru',
                  ('gaintseva.t@gmail.com',), fail_silently=False)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(1000.0, send_lost_messages_notification.s(), name="send_lost_messages_notification")