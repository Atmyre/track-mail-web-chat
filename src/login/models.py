from django.db import models
from django.contrib.auth.models import User, UserManager, AbstractBaseUser
import os
from django.utils import timezone
from chat.models import Chat, Membership
from message.models import Message
from rest_framework import serializers


def get_image_path(instance, filename):
    return os.path.join('users', str(instance.user.id), 'ava.jpg')


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    #avatar = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    last_activity = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.user.username

    def get_unread_messages(self):
        chats = Chat.objects.filter(chat_to_user__user=self.user)

        if len(chats) == 0:
            return ''

        message = "You got messages in {} chats, while you were offline:\n".format(len(chats))

        for chat in chats:
            lost_messages = Message.objects.filter(chat=chat, pub_date__gte=self.last_activity).order_by('pub_date')
            for lost_message in lost_messages:
                message += "In chat " + chat.name + " :\n" + "    " + lost_message.author.username + ": " + lost_message.text + '\n'

        return message


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('pk', 'user', 'last_activity')