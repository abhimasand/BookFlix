from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


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
    genres = models.CharField(max_length=500,default = "")
    current_page = models.CharField(max_length=10,default = "")
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Genres(models.Model):
    genre = models.CharField(max_length=50,default = "")

    def publish(self):
        self.save()

class CustomUser():
    username = models.CharField(('username'), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    liked_books = []
    wishlisted_books = []
    not_liked_books = []

    def publish(self):
        self.save()


