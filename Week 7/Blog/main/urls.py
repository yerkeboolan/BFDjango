from django.urls import path, re_path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('posts/new_post/', views.new_post, name='new_post'),
    path('todos/delete_all/', views.delete_all_posts, name='delete_all'),
    re_path(r'^posts/update/(\d+)/', views.update_post, name='update_post'),
    re_path(r'^posts/read_post/(\d+)/', views.post_detail, name='read_post'),
    re_path(r'^posts/delete_post/(\d+)/', views.delete_post, name='delete_post'),
    re_path(r'^todos/create_comment/(\d+)/', views.create_comment, name='create_comment'),

]