from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404

from .models import Task, AuditLog
from .forms import TaskForm


# ==========================
# HELPER FUNCTIONS
# ==========================
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def create_audit_log(request, action):
    AuditLog.objects.create(
        user=request.user if request.user.is_authenticated else None,
        action=action,
        ip_address=get_client_ip(request)
    )


def is_admin(user):
    return user.is_staff


# ==========================
# HOME PAGE
# ==========================
def home(request):
    return redirect('login')


# ==========================
# USER REGISTRATION
# ==========================
def register(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            AuditLog.objects.create(
                user=user,
                action="New user registered",
                ip_address=get_client_ip(request)
            )

            return redirect('login')

    else:
        form = UserCreationForm()

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )


# ==========================
# DASHBOARD
# ==========================
@login_required
def dashboard(request):

    tasks = Task.objects.filter(
        owner=request.user
    ).order_by('-created_at')

    total_tasks = tasks.count()

    pending_tasks = tasks.filter(
        status='pending'
    ).count()

    completed_tasks = tasks.filter(
        status='done'
    ).count()

    return render(
        request,
        'tasks/dashboard.html',
        {
            'tasks': tasks,
            'total_tasks': total_tasks,
            'pending_tasks': pending_tasks,
            'completed_tasks': completed_tasks
        }
    )


# ==========================
# CREATE TASK
# ==========================
@login_required
def task_create(request):

    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)
            task.owner = request.user
            task.save()

            create_audit_log(
                request,
                f"Created task: {task.title}"
            )

            return redirect('dashboard')

    else:
        form = TaskForm()

    return render(
        request,
        'tasks/task_form.html',
        {'form': form}
    )


# ==========================
# UPDATE TASK
# ==========================
@login_required
def task_update(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        owner=request.user
    )

    if request.method == 'POST':

        form = TaskForm(
            request.POST,
            instance=task
        )

        if form.is_valid():

            form.save()

            create_audit_log(
                request,
                f"Updated task: {task.title}"
            )

            return redirect('dashboard')

    else:
        form = TaskForm(instance=task)

    return render(
        request,
        'tasks/task_form.html',
        {
            'form': form,
            'task': task
        }
    )


# ==========================
# DELETE TASK
# ==========================
@login_required
def task_delete(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        owner=request.user
    )

    if request.method == 'POST':

        task_title = task.title
        task.delete()

        create_audit_log(
            request,
            f"Deleted task: {task_title}"
        )

        return redirect('dashboard')

    return render(
        request,
        'tasks/task_delete.html',
        {
            'task': task
        }
    )


# ==========================
# AUDIT LOG PAGE
# ADMIN ONLY
# ==========================
@login_required
@user_passes_test(is_admin)
def audit_log(request):

    logs = AuditLog.objects.all().order_by('-created_at')

    return render(
        request,
        'tasks/audit_log.html',
        {'logs': logs}
    )