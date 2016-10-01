from __future__ import unicode_literals

from django.db import models
from base.models import ModelWithLikes, PublicationModel
from comment.models import ModelWithComments
from event.models import EventModel


class Photo(ModelWithComments, EventModel, ModelWithLikes, PublicationModel):
    #author = models.ForeignKey(UserProfile, null=False)

    def get_descr(self):
        return str(author) + "has published a photo:"
