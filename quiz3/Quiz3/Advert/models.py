from django.db import models
from django.contrib.auth.forms import User

class Advert(models.Model):
    title = models.CharField('Title', max_length=50)
    address = models.CharField('Address', max_length=50)
    description = models.TextField()
    price = models.DecimalField('Price', max_digits=10, decimal_places=4)
    number_of_views = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' ' + self.description
