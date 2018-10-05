from django.urls import path, re_path
from main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('todos/', views.todos, name='todos'),
    re_path(r'^todos/(\d+)/completed/$', views.completed_todo, name='todo'),
    path('todos/completed', views.completed_todos, name='completed_todos'),
    re_path(r'^todos/([A-Za-z\_?]+)/filter/$', views.todos_filter, name='_filter'),
    re_path(r'^todos/(\d+)/change-mark/', views.change_mark, name='change_mark'),
    re_path(r'^todos/(\d+)/delete/', views.delete, name='delete'),
    path('todos/new/', views.todos_new, name='todo_new'),
]