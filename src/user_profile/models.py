# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractBaseUser
from photo.models import Photo
from rest_framework import serializers


'''
def get_image_path(instance, filename):
    return os.path.join('users', str(instance.user.id), 'ava.jpg')


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    avatar = models.ForeignKey(Photo, null=True, blank=True, verbose_name='userpic')
    friends = models.ManyToManyField("self", blank=True)

    def __unicode__(self):
        return self.user.username
'''

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')