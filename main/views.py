from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from .forms import MentorForm
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from .decorators import allowed_users, unauthenticated_user


def index(request):
    return render(request, 'main/new.html')


def celebrity(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/celebrity.html', {'title': 'Main page', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:
            error = 'Form is invalid'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/new_notes.html', context)


@allowed_users(allowed_roles=['Student'])
def find_mentor(request):
    error = ''
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
        else:

            error = 'Form is invalid'
    form = MentorForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/mentorFind.html', context)


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)
