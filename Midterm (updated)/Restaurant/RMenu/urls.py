from django.urls import path
from RMenu import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_restaurants/', views.show_restaurants, name='show_restaurants'),
    path('add_restaurant/', views.add_restaurant, name='add_restaurant'),
    path('<int:id>/update_restaurant/', views.update_restaurant, name='update_restaurant'),
    path('<int:id>/delete_restaurant/', views.delete_restaurant, name='delete_restaurant'),
]
