from django.contrib import admin
from .models import TodoList, Task

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(Task)