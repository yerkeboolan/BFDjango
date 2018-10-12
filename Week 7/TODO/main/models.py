from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class TodoList(models.Model):
    name = models.CharField("TODO List", max_length=50)
    created = models.DateTimeField("Date Created", auto_now=True)
    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField("Title", max_length=200)
    created = models.DateTimeField("Created", auto_now_add=True)
    due_on = models.DateTimeField("Due on", auto_now_add=False, editable=True)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='tasks')
    mark = models.BooleanField("Mark", default=False)

    def __str__(self):
        return self.title