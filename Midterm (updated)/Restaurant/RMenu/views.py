from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Restaurant, Dish, Review, RestaurantReview, DishReview
from .forms import RestaurantForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

def show_restaurants(request):
    rest = Restaurant.objects.all()
    context = {
        'restaurants': rest
    }
    return render(request, "restaurant/show.html", context)

@login_required
def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('show_restaurants')
    form = RestaurantForm()
    context = {
        'form': form,
    }
    return render(request, "restaurant/add.html", context)

@login_required
def update_restaurant(request, id):
    instance = get_object_or_404(Restaurant, pk=id)
    form = RestaurantForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('show_restaurants')
    context = {
        'form': form,
        'name': instance.name,
        'id': id,
    }
    return render(request, 'restaurant/update.html', context) 

@login_required
def delete_restaurant(request, id):
    Restaurant.objects.get(pk=id).delete()
    return redirect('show_restaurants')