from django import forms
from .models import Restaurant, Dish , RestaurantReview, DishReview

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'telephone', 'city')


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ('name', 'description', 'price', 'user', 'restaurant')

class RestaurantReviewForm(forms.ModelForm):
    class Meta:
        model = RestaurantReview
        fields = ('restaurant', 'review', 'user')

class DisReviewForm(forms.ModelForm):
    class Meta:
        model = DishReview
        fields = ('dish', 'review', 'user')