from django.urls import path
from Quiz3.api1 import views

urlpatterns = [
    path('login/', views.authentication, related_name='authentication')
]