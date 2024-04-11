from django.shortcuts import render, redirect, get_object_or_404
from .models import ToDoItem
from .forms import TaskForm, TaskUpdateForm

def task_list(request):
    tasks = ToDoItem.objects.all()
    tasks = ToDoItem.objects.order_by('deadline')
    return render(request, 'task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})


def delete_task(request, task_id):
    task = get_object_or_404(ToDoItem, pk=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task-list')

def update_task(request, task_id):
    task = get_object_or_404(ToDoItem, pk=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'update_task.html', {'form': form})