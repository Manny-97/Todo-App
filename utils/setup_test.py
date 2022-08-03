from django.test import TestCase


class TestSetup(TestCase):

    def setup(self):
        print('Test started')
        self.user = {
            'username': 'username',
            'email': 'email@hmail.com',
            'password': 'password'
            'password2': 'password'
        }
        # return super().setUp()


    def tearDown(self):
        print('Test finish')
        return super().tearDown()