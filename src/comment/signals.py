from django.db.models.signals import post_save
from .models import Comment


def comment_object_save(instance):
    instance.obj.comments_count += 1
    instance.obj.save()

for model in Comment.__subclasses__():
    post_save.connect(comment_object_save, model)
