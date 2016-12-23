from django.test import TestCase
from django.contrib.auth.models import User


class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_pages(self):
        response = self.client.get('/login/login/socialn/', follow=True)
        self.assertEqual(response.status_code, 200, "error: {}".format(response.status_code))

        response = self.client.get('/login/register/socialn/', follow=True)
        self.assertEqual(response.status_code, 200, "error: {}".format(response.status_code))

        user = User.objects.create_user(username="test", password="test", email="test@yandex.ru")
        response = self.client.post('/login/login/socialn/', {'username': user.username, 'password': 'test'},
                                    follow=True)
        response = self.client.get('/socialn/', follow=True)
        self.assertEqual(response.status_code, 200, "error: {}".format(response.status_code))