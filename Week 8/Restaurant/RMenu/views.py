from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Restaurant, Dish, Review, RestaurantReview, DishReview
from .forms import RestaurantForm
from django.views import View
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView, DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class IndexView(TemplateView):
    template_name = "index.html"


class RestaurantList(ListView):
    model = Restaurant
    context_object_name = 'restaurants'
    template_name = 'restaurant/show.html'


@method_decorator(login_required, name='dispatch')
class RestaurantCreateView(CreateView):
    login_required = True
    model = Restaurant
    form_class = RestaurantForm
    template_name = "restaurant/create.html"


    def form_valid(self ,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = "restaurant/show.html"


@method_decorator(login_required, name='dispatch')
class RestaurantUpdateView(UpdateView):
    login_required = True
    model = Restaurant
    fields = ['name', 'telephone', 'city']
    template_name = "restaurant/update.html"

@method_decorator(login_required, name='dispatch')
class RestaurantDeleteView(DeleteView):
    login_required = True
    model = Restaurant
    template_name = "restaurant/confirm.html"
    success_message = "Thing was deleted successfully"


    def get_success_url(self):
        return reverse("show_restaurants")