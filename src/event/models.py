# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from user_profile.models import User
from base.models import ModelWithLikes, PublicationModel
from comment.models import ModelWithComments
from rest_framework import serializers
import datetime
from time import timezone
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class EventModel(models.Model):
    class Meta:
        abstract = True

    def get_author(self):
        pass

    def get_title(self):
        pass

    def get_repr(self):
        pass


class Event(ModelWithLikes, ModelWithComments, PublicationModel):
    title = models.CharField(max_length=100, verbose_name='event_title', default='none')
    text = models.TextField(verbose_name='event_text')
    user_to_show = models.ForeignKey(User, null=False, verbose_name="user_to_show_event")

    #content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    #content_object = GenericForeignKey('content_type', 'object_id')

    published = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def message_beginning(self):
        return self.text[:50]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'text', 'user_to_show', 'published', 
            'likes_count', 'pub_date', 'mod_date', 'comments_count', 'comments')
