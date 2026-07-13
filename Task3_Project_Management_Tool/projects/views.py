from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse

from .models import Project, Membership, Task, TaskComment, Notification
from .forms import RegisterForm, ProjectForm, TaskForm, TaskCommentForm, AddMemberForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, 'Account created.')
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'projects/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'projects/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def _notify(user, message):
    Notification.objects.create(user=user, message=message)


def _is_member(project, user):
    return project.members.filter(id=user.id).exists()


@login_required
def dashboard_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            Membership.objects.create(project=project, user=request.user, role='owner')
            messages.success(request, f'Project "{project.name}" created.')
            return redirect('dashboard')
    else:
        form = ProjectForm()

    projects = Project.objects.filter(members=request.user)
    return render(request, 'projects/dashboard.html', {'projects': projects, 'form': form})


@login_required
def project_board(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if not _is_member(project, request.user):
        messages.error(request, "You're not a member of this project.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = TaskForm(request.POST, project=project)
        if form.is_valid():
            task = form.save(commit=False)
            task.project = project
            task.created_by = request.user
            task.save()
            if task.assigned_to:
                _notify(task.assigned_to, f'You were assigned to "{task.title}" in {project.name}')
            messages.success(request, 'Task created.')
            return redirect('project_board', project_id=project.id)
    else:
        form = TaskForm(project=project)

    tasks = project.tasks.all()
    columns = {
        'todo': tasks.filter(status='todo'),
        'in_progress': tasks.filter(status='in_progress'),
        'done': tasks.filter(status='done'),
    }

    return render(request, 'projects/board.html', {
        'project': project,
        'columns': columns,
        'form': form,
    })


@login_required
def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if not _is_member(task.project, request.user):
        return JsonResponse({'error': 'not a member'}, status=403)

    new_status = request.POST.get('status')
    if new_status in dict(Task.STATUS_CHOICES):
        task.status = new_status
        task.save()
        return JsonResponse({'ok': True, 'status': task.get_status_display()})
    return JsonResponse({'error': 'invalid status'}, status=400)


@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if not _is_member(task.project, request.user):
        messages.error(request, "You're not a member of this project.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = TaskCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.task = task
            comment.author = request.user
            comment.save()
            # let the assignee know someone commented
            if task.assigned_to and task.assigned_to != request.user:
                _notify(task.assigned_to, f'{request.user.username} commented on "{task.title}"')
            return redirect('task_detail', task_id=task.id)
    else:
        form = TaskCommentForm()

    comments = task.comments.all()
    return render(request, 'projects/task_detail.html', {
        'task': task,
        'comments': comments,
        'form': form,
    })


@login_required
def add_member(request, project_id):
    project = get_object_or_404(Project, id=project_id, owner=request.user)
    if request.method == 'POST':
        form = AddMemberForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            try:
                user_to_add = User.objects.get(username=username)
                Membership.objects.get_or_create(project=project, user=user_to_add, defaults={'role': 'member'})
                _notify(user_to_add, f'You were added to project "{project.name}"')
                messages.success(request, f'{username} added to the project.')
            except User.DoesNotExist:
                messages.error(request, f'No user found with username "{username}".')
    return redirect('project_board', project_id=project.id)


@login_required
def notifications_view(request):
    notifications = request.user.notifications.all()[:20]
    request.user.notifications.filter(is_read=False).update(is_read=True)
    return render(request, 'projects/notifications.html', {'notifications': notifications})


@login_required
def notifications_poll(request):
    """Small JSON endpoint the dashboard polls every so often for the unread badge."""
    unread_count = request.user.notifications.filter(is_read=False).count()
    return JsonResponse({'unread_count': unread_count})
