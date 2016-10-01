from __future__ import unicode_literals

from django.db import models
from base.models import EmailSenderModel
from user_profile.models import User

class Like(EmailSenderModel):
    author = models.ForeignKey(User, null=False)

