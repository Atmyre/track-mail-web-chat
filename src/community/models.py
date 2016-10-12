# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from user_profile.models import User
from photo.models import Photo
from event.models import Event
from rest_framework import serializers

class Community(models.Model):
    name = models.TextField(verbose_name='community_name')
    avatar = models.ForeignKey(Photo, null=True, blank=True, verbose_name='avatar')
    users = models.ManyToManyField(User, blank=False)
    events = models.ManyToManyField(Event, blank=True)

    created_at = models.DateTimeField(verbose_name='community_creation_time', auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="community_inviter")

class Membership(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="community_to_user")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_to_community")
    inviter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="membership_community_invites",
    )

class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = ('name', 'users', 'avatar', 'created_at', 'creater', 'events')