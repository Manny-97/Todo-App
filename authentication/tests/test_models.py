from django.test import TestCase
from authentication.models import User
from django.test import TestCase

class TestModel(TestCase):

    def test_should_create_user(self):
        

        self.assertEqual(str(user), 'email@app.com')


