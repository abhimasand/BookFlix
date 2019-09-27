from django.conf import settings
from django.db import models
from django.utils import timezone


class Book(models.Model):
    book_id = models.CharField(max_length=200,default = "")
    goodreads_book_id = models.CharField(max_length=200,default = "")
    published_date = models.CharField(max_length=200,default = "")
    author = models.CharField(max_length=200,default = "")
    title = models.CharField(max_length=200,default = "")
    original_title = models.CharField(max_length=200,default = "")
    rating = models.CharField(max_length=200,default = "")
    description = models.TextField(default = "")
    image_url = models.CharField(max_length=200,default = "")
    image_location = models.CharField(max_length=200,default = "")
    status = models.CharField(max_length=200,default = "Not Read")
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title