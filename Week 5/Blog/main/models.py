from django.db import models

class User(models.Model):
    first_name = models.CharField("First Name", max_length=50)
    last_name = models.CharField("Last Name", max_length = 50)
    nickname = models.CharField("Nickname", max_length=50)
    birth_date = models.DateField('Birth Date', auto_now=False, auto_now_add=False)
    email = models.EmailField("Email Adress", max_length=254)
    password = models.CharField("Password", max_length=50)


class Author(User):
    rating = models.FloatField("Rating")


class Follower(User):
    authors = models.ManyToManyField(Author, verbose_name= "authors")



class Text(models.Model):
    content = models.TextField("Content")
    author = models.ManyToManyField(Author, verbose_name="authors")
    rating = models.FloatField("Rating")

class Post(Text):
    title = models.CharField("Title", max_length=50)
    date_published = models.DateTimeField("Date Published", auto_now=True, auto_now_add=False)