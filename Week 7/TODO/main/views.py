from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import TodoList, Task
from .forms import TodoListForm, TaskForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "index.html")

@login_required
def to_do_lists(request):
    todo_lists = TodoList.objects.all()
    context = {
        'todo_lists': todo_lists,
    }
    return render(request, 'todo_list/show.html', context)

def add_todo_list(request):
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('todo_lists')
    form = TodoListForm
    context = {
        'form': form,
    }
    return render(request, "todo_list/add.html", context)

def delete_todo_list(request, id):
    TodoList.objects.get(pk=id).delete()
    return redirect('todo_lists')


def update_todo_list(request, id):
    instance = get_object_or_404(TodoList, pk=id)
    form = TodoListForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('todo_lists')
    context = {
        'form': form,
        'name': instance.name,
        'id': id,
    }
    return render(request, 'todo_list/update.html', context)

def tasks(request, id):
    ilist = TodoList.objects.get(pk=id)
    tasks = ilist.tasks.all()
    context = {
        'tasks': tasks,
        'ilist': ilist,
    }
    return render(request, "task/show.html", context)

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('tasks', 1)
    form = TaskForm()
    context = {
        'form': form,
    }
    return render(request, "task/add.html", context)

def delete_task(request, id):
    Task.objects.get(pk=id).delete()
    return redirect('tasks', 1)

def update_task(request, id):
    instance = get_object_or_404(Task, pk=id)
    form = TaskForm(request.POST or None, instance=instance)
    if request.method == 'POST':
        if form.is_valid:
            form.save()
            return redirect('tasks', 1)
    context = {
        'form': form,
        'name': instance.title,
        'id': id,
    }
    return render(request, 'task/update.html', context)

def change_mark(request, id):
    ilist = TodoList.objects.get(pk=1)
    tasks = ilist.tasks.all()
    task = tasks.get(pk=id)
    if task.mark:
        task.mark = False
    else:
        task.mark = True
    task.save()
    return redirect('tasks', 1)

def order(request, order_by):
    return