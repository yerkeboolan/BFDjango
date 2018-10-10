from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:author_id>', views.author_detail, name='author_detail'),
    path('authors/new/', views.author_new, name='author_new'),

    path('books/', views.book_list, name='book_list'),
    path('show_color/', views.show_color),
    path('set_color/', views.set_color),

]
