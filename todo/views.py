from django.shortcuts import render, redirect,get_object_or_404
from .models import Todo

# Create your views here.
def create_task(request):
   title = request.POST.get('title')
   Todo.objects.create(title=title)
   return redirect('home')
    

def completed_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    task.completed = True
    task.save()
    return redirect('home')
    
def delete_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    else:
        
        return redirect('home')
    
def uncompleted_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    task.completed = False
    task.save()  
    return redirect('home')

def update_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    todos = Todo.objects.filter(completed=False)
    completed = Todo.objects.filter(completed=True)
    context = {
        'task': task,
        'todos': todos,
        'completed_tasks': completed,
    }
    return render(request,'task-edit.html',context)

def edit_task(request, task_id):
    task = get_object_or_404(Todo, id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title','').strip()
        if title :
            task.title = title
            task.save()
        return redirect('home')
    
    return redirect('update_task', task_id=task.id)