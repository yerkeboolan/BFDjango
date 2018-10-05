from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Task
from django.views.decorators.csrf import csrf_exempt
from django.urls import resolve
from .forms import TaskForm

def index(request):
    return render(request, "base.html")

def todos(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, "task/list.html", context)


def completed_todos(request):
    tasks = [i for i in Task.objects.all() if i.mark]
    context = {
        'tasks': tasks
    }
    return render(request, "task/completed_list.html", context)

def completed_todo(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, "task/completed.html", {'task': task})


def todos_filter(request, filter_by):
    tasks = Task.objects.order_by(filter_by)
    context = {
        'tasks': tasks
    }
    return render(request, "task/list.html", context)

def change_mark(request, id):
    task = Task.objects.get(pk=id)
    if task.mark:
        task.mark = False
    else:
        task.mark = True
    task.save()
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, "task/list.html", context)

def delete(request, id):
    Task.objects.get(pk=id).delete()
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, "task/list.html", context)

def todos_new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
    else:
        form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'task/new.html', context)