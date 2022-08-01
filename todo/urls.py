from django.urls import path
from .views import index, create_todo, todo_detail, todo_delete

urlpatterns = [
    path('', index, name='home'),
    path('create/', create_todo, name='create-todo'),
    path('todo/<id>/', todo_detail, name='todo'),
    path('todo-delete/<id>/', todo_delete, name="todo-delete")
]