from django.db.models.signals import post_save

from .models import EmailSenderModel
from __future__ import absolute_import
from celery import shared_task

from django.core.mail import send_mail

@shared_task
def send_email(instance, created=False):
    if created:
        pass

@receiver(models.signals.post_save, sender=Answer)
def on_answer_creation(sender, instance, *args, **kwargs):
    if kwargs.get('created'):
        answer = instance
        from .tasks import send_email_notification
        send_email_notification.delay(
            'd.isaev@corp.mail.ru',
            'New answer to question "{}"'.format(answer.question.title),
            'You got answer with the text: "{}"'.format(answer.text)
        )


def liked_object_save(instance):
    instance.obj.likes_count += 1
    instance.obj.save()


for model in EmailSenderModel.__subclasses__:
    post_save.connect(send_email, model)