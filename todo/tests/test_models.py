from django.test import TestCase
from matplotlib.pyplot import title
from authentication.models import User
from django.test import TestCase
from todo.models import Todo
class TestModel(TestCase):

    def test_should_create_user(self):
        user = User.objects.create_user(username='username', email='email@app.com')
        user.set_password('password12!')
        user.save()

        todo = Todo(owner=user, title='Buy milk', description='get it done')

        todo.save()

        self.assertEqual(str(todo), 'Buy milk')

