# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers


class Chat(models.Model):
    name = models.TextField(verbose_name='chat_name')
    users = models.ManyToManyField(
        User,
        through='Membership',
        through_fields=('chat', 'user'),
    )

    author = models.ForeignKey(User, related_name='chats')

    creation_date = models.DateTimeField(verbose_name='chat_creation_time', auto_now_add=True)

    def get_channel_name(self):
        return "chat-channel-{}".format(self.id)


class Membership(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="chat_to_user")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_to_chat")
    user_chat_id = models.IntegerField(null=False)
    inviter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="membership_chat_invites",
    )


class ChatSerializer(serializers.ModelSerializer):

    channel_name = serializers.ReadOnlyField(source="get_channel_name")

    class Meta:
        model = Chat
        fields = ('pk', 'name', 'users', 'author', 'channel_name')
