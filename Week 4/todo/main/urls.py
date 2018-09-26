from django.urls import path, re_path
from main import views

urlpatterns = [
    path('todos/', views.todos),
    re_path(r'^todos/(\d+)/completed/$', views.completed_todos),
]
