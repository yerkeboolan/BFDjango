from django.urls import path, re_path
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo_lists/', views.to_do_lists, name='todo_lists'),
    path('add_todo_list/', views.add_todo_list, name='add_todo_list'),
    path('<int:id>/delete_todo_list/', views.delete_todo_list, name='delete_todo_list'),
    path('<int:id>/update_todo_list/', views.update_todo_list, name='update_todo_list'),
    path('todo_lists/<int:id>/tasks/', views.tasks, name='tasks'),
    path('todo_list/add_task/', views.add_task, name='add_task'),
    path('todo_lists/<int:id>/delete_task/', views.delete_task, name='delete_task'),
    path('todo_lists/<int:id>/update_task/', views.update_task, name='update_task'),
    path('todo_lists/<int:id>/change_mark/', views.change_mark, name='change_mark'),
    path('<str:order_by>/order/', views.order, name='order'),
]