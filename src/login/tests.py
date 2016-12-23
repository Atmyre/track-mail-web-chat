from django.test import TestCase
from django.contrib.auth.models import User


class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_login(self):
        user = User.objects.create_user(username="test", password="test", email="test@yandex.ru")
        response = self.client.post('/login/login/socialn/', {'username': user.username, 'password': 'test'},
                                    follow=True)
        self.assertEqual(response.status_code, 200, "error: {}".format(response.status_code))

        response = self.client.get('/socialn/')
        self.assertContains(response, user.username)

        response = self.client.get('/login/logout/socialn/', follow=True)
        self.assertEqual(response.status_code, 200, "error: {}".format(response.status_code))

        response = self.client.get('/socialn/')
        self.assertNotContains(response, user.username)

        response = self.client.post('/login/login/socialn/', {'username': user.username, 'password': 'testtest'},
                                    follow=True)
        self.assertContains(response, "Your username and/or password are incorrect")

    def test_register(self):
        response = self.client.post('/login/register/socialn/', {'username': "test1", 'password': 'test1',
                                                                 'email': 'test1@yandex.ru'}, follow=True)

        self.assertEqual(response.status_code, 200, "error: {}".format(response.status_code))
        self.assertTrue(User.objects.filter(username='test1').first() is not None)