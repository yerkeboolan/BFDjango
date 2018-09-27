from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Task


def todos(request):
    todo_list = Task.objects.all()

    context = {
        'todo_list': todo_list,
    }

    return render(request, 'todo_list.html', context)


def completed_todos(request, index):
    task = Task.objects.all() [int(index)]
    context = {
        'task': task
    }
    return render(request, 'completed_todo_list.html', context)
