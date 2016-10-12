from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from base.models import TextModel, EmailSenderModel, PublicationModel
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class Comment(TextModel, EmailSenderModel, PublicationModel):
    event = models.ForeignKey('event.Event', null=False)
    item_type = models.ForeignKey(ContentType)
    item_id = models.PositiveIntegerField()


class ModelWithComments(models.Model):
    class Meta:
        abstract = True

    comments_count = models.IntegerField(default=0, verbose_name="comments_count")
    comments = GenericRelation(Comment, content_type_field='item_type', object_id_field='item_id')

    def recalculate_comments_count(self):
        self.comments_count = self.comments.count()

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('item_id', 'item_type', 'event', 'text', 'author')
