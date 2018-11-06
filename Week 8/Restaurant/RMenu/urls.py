from django.urls import path
from RMenu import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('restaurants/', views.RestaurantList.as_view(), name='show_restaurants'),
    path('restaurant/create/', views.RestaurantCreateView.as_view(), name='create_restaurant'),
    path('restaurant/detail/<int:pk>/', views.RestaurantDetailView.as_view(), name='detail_restaurant'),
    path('restaurant/update/<int:pk>/', views.RestaurantUpdateView.as_view(), name='update_restaurant'),
    path('restaurant/delete/<int:pk>/', views.RestaurantDeleteView.as_view(), name='delete_restaurant'),

]