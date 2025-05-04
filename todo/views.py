from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, CustomSignupForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# def home_redirect(request):
#     if request.user.is_authenticated:
#         return redirect('task_list')  
#     return redirect('signup')
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')

    incomplete_tasks = Task.objects.filter(user=request.user, completed=False).order_by('-created_at')
    completed_tasks = Task.objects.filter(user=request.user, completed=True).order_by('-created_at')

    return render(request, 'todo/task_list.html', {
        'form': form,
        'incomplete_tasks': incomplete_tasks,
        'completed_tasks': completed_tasks,
    })

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    return render(request, 'todo/task_detail.html', {'task': task})

@login_required
def toggle_task_completion(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = CustomSignupForm()
    
    return render(request, 'registration/signup.html', {'form': form})