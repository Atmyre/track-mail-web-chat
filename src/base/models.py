# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
import datetime


class PublicationModel(models.Model):
    class Meta:
        abstract = True

    pub_date = models.DateTimeField(verbose_name='creation_date', default=timezone.now)
    mod_date = models.DateTimeField(verbose_name='modification_date', default=timezone.now)


class EmailSenderModel(models.Model):
    class Meta:
        abstract = True

    def send_email(self):
        pass


class ModelWithLikes(models.Model):

    class Meta:
        abstract = True

    likes_count = models.IntegerField(default=0, verbose_name="likes_count")


class TextModel(models.Model):

    class Meta:
        abstract = True

    text = models.TextField(verbose_name='message_text')
    author = models.ForeignKey(User, null=True, blank=True, verbose_name='message_author')

    published = models.BooleanField(default=True)

    def __str__(self):
        return self.text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def message_beginning(self):
        return self.text[:50]
