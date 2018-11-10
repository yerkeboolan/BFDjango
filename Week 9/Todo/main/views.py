from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, Task
from django.views import View
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class IndexView(TemplateView):
    template_name = "index.html"

class TodoListView(ListView):
    model = TodoList
    context_object_name = 'todo_lists'
    template_name = 'todo_list/show.html'


@method_decorator(login_required, name='dispatch')
class TodoListCreateView(CreateView):
    login_required = True
    model = TodoList
    form_class = TodoList
    template_name = "todo_list/add.html"

    def form_valid(self ,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class TodoListDetailView(DetailView):
    model = TodoList
    template_name = "todo_list/show.html"


@method_decorator(login_required, name='dispatch')
class TodoListUpdateView(UpdateView):
    login_required = True
    model = TodoList
    fields = ['name', 'created']
    template_name = "todo_list/update.html"






class TaskListView(ListView):
        model = Task
        context_object_name = 'tasks'
        template_name = 'tasks/show.html'



@method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):
        login_required = True
        model = Task
        form_class = Task
        template_name = "task/add.html"

        def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)

        def form_invalid(self, form):
            return super().form_invalid(form)

class TaskDetailView(DetailView):
        model = Task
        template_name = "task/show.html"

@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
        login_required = True
        model = Task
        fields = ['title', 'created', 'due_on']
        template_name = "task/update.html"




