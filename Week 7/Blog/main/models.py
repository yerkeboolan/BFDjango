from django.db import models
import datetime

from datetime import timezone
now = datetime.datetime.now()
class Posts(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateTimeField(default=now)
    '''
    STATUS_CHOICE = (
        ('Published', 'published'),
        ('Draft', 'draft'),
    )
    status = models.CharField(max_length=50, choices=STATUS_CHOICE)
    '''
    def __str__(self):
        return "#{}: {}".format(self.title, self.author)
class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    created_date = models.DateTimeField(default=now)
    comment_text = models.TextField()
    #many to one relationship
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments', null=True)

    def __str__(self):
        return "#{}: {}".format(self.name, self.email)