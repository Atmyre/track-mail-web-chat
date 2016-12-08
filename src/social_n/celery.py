from __future__ import absolute_import
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_n.settings')

from django.conf import settings

app = Celery('social_n')
app.config_from_object('django.conf:settings')
#app.config_from_object('celeryconfig')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_n.settings')
#app = Celery('social_n', broker='redis://localhost:6379/0')



