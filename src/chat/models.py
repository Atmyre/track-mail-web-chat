# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from user_profile.models import User

class Chat(models.Model):
    name = models.TextField(verbose_name='chat_name')
    users = models.ManyToManyField(User, blank=False)

    creation_date = models.DateTimeField(verbose_name='chat_creation_time', auto_now_add=True)

class Membership(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="chat_to_user")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_to_chat")
    inviter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="membership_chat_invites",
    )
