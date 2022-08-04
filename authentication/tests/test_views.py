from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from utils.setup_test import TestSetup

class TestViews(TestSetup):

    def test_should_show_register_page(self):
        # user1 = self.create_test_user()
        # user2 = self.create_test_two()


        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')

    def test_should_show_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')

    

    