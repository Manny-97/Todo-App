from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Todo
from .forms import TodoForm
from django.urls import reverse

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    completed_count = todos.filter(is_completed=True).count()
    incomplete_count = todos.filter(is_completed=False).count()
    all_count = todos.count()

    
    context = {'todos': todos, 'all_count': all_count,
                'completed_count': completed_count, 'incomplete_count': incomplete_count}
    return render(request, 'todo/index.html', context)

def create_todo(request):
    form = TodoForm()
    context = {'form': form}

    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed', False)

        todo = Todo()

        todo.title = title
        todo.description = description
        todo.is_completed = True if is_completed == "on" else False

        todo.save()

        return HttpResponseRedirect(reverse("todo", kwargs={"id": todo.pk}))

    return render(request, 'todo/create-todo.html', context)


def todo_detail(request, id):
    return render(request, 'todo/todo-detail.html', {})