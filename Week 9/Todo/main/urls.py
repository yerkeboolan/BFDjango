from django.urls import path
from main import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('todo_list/', views.ListView.as_view(), name='show_todo_list'),
    path('todo_list/create/', views.CreateView.as_view(), name='create_todo_list'),
    path('todo_list/detail/<int:pk>/', views.DetailView.as_view(), name='detail_todo_list'),
    path('todo_list/update/<int:pk>/', views.UpdateView.as_view(), name='update_todo_list'),

    path('', views.IndexView.as_view(), name='index'),
    path('tasks/', views.ListView.as_view(), name='show_task'),
    path('task/create/', views.CreateView.as_view(), name='create_task'),
    path('task/detail/<int:pk>/', views.DetailView.as_view(), name='detail_task'),
    path('task/update/<int:pk>/', views.UpdateView.as_view(), name='update_task'),
]