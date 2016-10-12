from __future__ import unicode_literals

from django.db import models
from base.models import EmailSenderModel
from user_profile.models import User
from rest_framework import serializers

class Like(EmailSenderModel):
    author = models.ForeignKey(User, null=False)

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'author')

