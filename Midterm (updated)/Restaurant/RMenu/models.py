from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Restaurant(models.Model):
    name = models.CharField("Name", max_length=50)
    telephone = models.CharField('Telephone', max_length=50)
    city = models.CharField("City", max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='restaurants')

class Dish(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.TextField("Description")
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_dishes')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_dishes')


class Review(models.Model):
    rating = models.FloatField()
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True, editable=True)

class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='rest_rest_revs')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_rest_revs')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_rest_revs')

class DishReview(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='dish_dish_revs')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='review_dish_revs')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_dish_revs')

