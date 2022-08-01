from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Todo
from .forms import TodoForm
# Create your views here.
def index(request):
    return render(request, 'todo/index.html')

def create_todo(request):
    form = TodoForm()
    context = {'form': form}

    if request.method == "POST":
        titles = request.POST.get('title')
        description = request.POST.get('description')
        is_completed = request.POST.get('is_completed', False)

        todo = Todo()

        todo.title = title
        todo.description = description
        todo.is_completed = True if is_completed == "on" else False

        todo.save()

        return HttpResponseRedirect('')

    return render(request, 'todo/create-todo.html', context)


