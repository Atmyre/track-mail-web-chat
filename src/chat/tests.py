from django.test import TestCase
from .models import Chat, User, Membership


class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_chat_access(self):
        user1 = User.objects.create_user(username="test1", password="test1", email="test1@yandex.ru")
        user2 = User.objects.create_user(username="test2", password="test2", email="test2@yandex.ru")

        chat = Chat(name="test_chat", author=user1)
        chat.save()

        membership = Membership(chat=chat, user=user1, user_chat_id=1, inviter=user1)
        membership.save()

        self.client.login(username=user1.username, password="test1")
        response = self.client.get('/api/chat/'+str(chat.id)+'/')
        self.assertEqual(response.status_code, 200, "error: {}".format(response.status_code))
        self.client.logout()

        self.client.login(username=user2.username, password="test2")
        response = self.client.get('/api/chat/'+str(chat.id)+'/')
        self.assertNotEqual(response.status_code, 200, "error: {}".format(response.status_code))
        self.client.logout()




