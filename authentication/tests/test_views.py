from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from utils.setup_test import TestSetup

class TestViews(TestSetup):

    def test_should_show_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')


    def test_should_show_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')

    def test_should_signup_user(self):
        self.user = {
            'username': 'username',
            'email': 'email@hmail.com',
            'password': 'password',
            'password2': 'password'
        }
        response = self.client.post(reverse('register'), self.user)
        self .assertEqual(response.status_code, 302)


    def test_should_not_signup_user_with_taken_username(self):
        self.user = {
            'username': 'username',
            'email': 'email@hmail2.com',
            'password': 'password',
            'password2': 'password'
        }
        self.client.post(reverse('register'), self.user)
        response = self.client.post(reverse('register'), self.user)
        self .assertEquals(response.status_code, 409)