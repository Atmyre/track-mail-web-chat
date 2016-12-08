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
    user_to_show = models.ForeignKey(User, null=False, verbose_name="user_to_show_event")

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    published = models.BooleanField(default=True)

    def __str__(self):
        return str(self.pub_date)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def message_beginning(self):
        return self.text[:50]

    def get_descr(self):
        mod = ContentType.get_object_for_this_type(self.content_type, id=self.object_id)
        print(mod.get_descr())
        #if self.content_object.get_content_type() == ''
        return mod.get_descr()


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'title', 'text', 'user_to_show', 'published', 
            'likes_count', 'pub_date', 'mod_date', 'comments_count', 'comments')
