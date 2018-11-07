from django import forms
from .models import TodoList, Task

class ToDoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('name', 'user')


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'due_on', 'todo_list', 'mark')


