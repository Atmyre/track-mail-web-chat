# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from user_profile.models import User
from event.models import EventModel


class Relation(EventModel):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_from")
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_to")

    start_date = models.DateTimeField(verbose_name='relation_start_date', auto_now_add=True)
    are_friends = models.BooleanField(default=False)
    end_date = models.DateTimeField(verbose_name='relation_end_date', null=True, auto_now_add=True)

    def get_descr(self):

        return "User "

