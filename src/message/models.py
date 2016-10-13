# coding: utf-8
from __future__ import unicode_literals
from user_profile.models import User
from like.models import Like
from chat.models import Chat
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
import datetime

from django.db import models
from base.models import EmailSenderModel, ModelWithLikes, TextModel
from comment.models import ModelWithComments
from rest_framework import serializers



class Message(ModelWithComments, EmailSenderModel, TextModel, ModelWithLikes):

    chat = models.ForeignKey(Chat, null=True, blank=True, verbose_name='message_chat', on_delete=models.CASCADE)

class MessageSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.id')

	class Meta:
		model = Message
		fields = ('id', 'chat', 'author', 'text', 'likes_count')
