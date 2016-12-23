from django.test import TestCase
from django.contrib.auth.models import User
from friends.models import Relation
from .models import Event


class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_event_signal(self):
        user1 = User.objects.create_user(username="test1", password="test1", email="test1@yandex.ru")
        user2 = User.objects.create_user(username="test2", password="test2", email="test2@yandex.ru")

        relation = Relation(user_from=user1, user_to=user2, author=user1, are_friends=True)
        relation.save()

        event = Event.objects.filter(user_to_show=user1).first()
        self.assertTrue(event.content_object == relation)
