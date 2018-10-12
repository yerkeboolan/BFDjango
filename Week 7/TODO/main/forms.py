from django import forms
from datetimepicker.widgets import DateTimePicker
from .models import TodoList, Task


class TodoListForm(forms.ModelForm):
    class Meta:
        model = TodoList
        fields = ('name',)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'due_on', 'todo_list', 'mark')
