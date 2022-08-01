from django.urls import path
from .views import index, create_todo, todo_detail

urlpatterns = [
    path('', index, name='home'),
    path('create/', create_todo, name='create-todo'),
    path('todo/<id>/', todo_detail, name='todo'),
]