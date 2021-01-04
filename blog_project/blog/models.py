from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#class in database, own table in data base
class Post(models.Model):
    #field in table
    title = models.CharField(max_length =100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #if user if delete, delete their post to

    def __str__(self):
        return self.title