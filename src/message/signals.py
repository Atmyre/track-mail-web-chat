from django.db.models.signals import post_save

from .models import Message
from adjacent import Client
from .models import MessageSerializer


def create_message(instance, **kwargs):
    client = Client()
    client.publish(instance.chat.get_channel_name(), MessageSerializer(instance).data)
    response = client.send()
    print('sent to channel {}, got response from centrifugo: {}'.format(instance.chat.get_channel_name(),
                                                                        response))


def init_signals():
    post_save.connect(create_message, sender=Message)
