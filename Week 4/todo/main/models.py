from django.db import models

class Author(models.Model):
    firstname = models.CharField("First Name", max_length=50)
    lastname = models.CharField("Last Name", max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.firsname + ' ' + self.lastname



class Task(models.Model):
    title = models.CharField("Title", max_length=200)
    created = models.DateTimeField("Created", auto_now_add=True)
    due_on = models.DateTimeField("Due on", auto_now_add=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    mark = models.BooleanField("Mark", default=False)

    def __str__(self):
        return self.title