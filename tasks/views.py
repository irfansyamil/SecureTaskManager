from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


@login_required
def dashboard(request):
    tasks = Task.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'tasks/dashboard.html', {'tasks': tasks})


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('dashboard')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_update(request, task_id):
    task = Task.objects.get(id=task_id, owner=request.user)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_delete(request, task_id):
    task = Task.objects.get(id=task_id, owner=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('dashboard')

    return render(request, 'tasks/task_delete.html', {'task': task})