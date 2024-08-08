from django.shortcuts import render,redirect
from.models import Task

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'todo/index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        Task.objects.create(title=title)
    return redirect('index')

def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.completed = 'completed' in request.POST
        task.save()
        return redirect('index')
    return render(request, 'todo/update_task.html', {'task': task})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('index')
