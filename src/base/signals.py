from django.db.models.signals import post_save

from .models import EmailSenderModel, ModelWithComment


def send_email(instance, created=False):
    if created:
        pass


def liked_object_save(instance):
    instance.obj.likes_count += 1
    instance.obj.save()


for model in EmailSenderModel.__subclasses__:
    post_save.connect(send_email, model)