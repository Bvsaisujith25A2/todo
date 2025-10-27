from django.shortcuts import render
from todo.models import Todo



def home(request):
    todos = Todo.objects.filter(completed=False)
    completed = Todo.objects.filter(completed=True)
    context = {
        'todos': todos,
        'completed_tasks': completed,
    }
    return render(request, 'home.html',context)