from django.contrib import admin
from .models import Restaurant, Dish, Review, RestaurantReview, DishReview

admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Review)
admin.site.register(RestaurantReview)
admin.site.register(DishReview)