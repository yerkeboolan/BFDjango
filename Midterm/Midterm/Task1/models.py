from django.db import models

class User(models.Model):
    firstname=models.CharField("Firstname", max_length=50)
    lastname=models.CharField("Lastname", max_length=50)
    email=models.EmailField()

    def __str__(self):
        return self.firstname + ' ' + self.lastname

class Restaurant(models.Model):
    name = models.CharField("Name", max_length=50)
    number = models.IntegerField()
    telephone = models.IntegerField()
    city = models.CharField("City", max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField("Name", max_length=50)
    description = models.CharField("Description", max_length=250)
    price  = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant  = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant

class Review(models.Model):
    rating = models.FloatField()
    comment = models.CharField("Comment", max_length=150)
    date = models.DateTimeField("Date", auto_now_add=True)

    def __str__(self):
        return self.date + ' ' + self.rating

class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.review

class DishReview(models.Model):
    dish = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.review
