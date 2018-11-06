from django import forms
from .models import Restaurant, Dish, Review, RestaurantReview, DishReview

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'telephone', 'city', 'user',)

# class DishForm(forms.ModelForm):
#     class Meta:
#         model = Dish
#         fields = ('name', 'description', 'price', 'user', 'restaurant',)


# class ReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ('rating', 'comment', 'date',)

# class RestaurantReviewForm(forms.ModelForm):
#     class Meta:
#         model = RestaurantReview
#         fields = ('restaurant', 'review', 'user',)

# class DishReviewForm(forms.ModelForm):
#     class Meta:
#         model = DishReview
#         fields = ('dish', 'review', 'user',)

