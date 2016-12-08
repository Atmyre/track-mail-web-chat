from celery.schedules import crontab

# celery
BROKER_URL = 'redis://localhost:6379/0'
CELERY_CACHE_BACKEND = 'redis://localhost:6379/1'
#CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'


from message.tasks import send_lost_messages_notification
CELERYBEAT_SCHEDULE = {
    'every-minute': {
        'task': 'send_lost_messages_notification',
        'schedule': crontab(minute='*/1'),
        'args': (),
    },
}