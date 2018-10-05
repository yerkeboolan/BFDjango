from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'due_on', 'author', 'mark')
        widgets = {
            'due_on': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }
