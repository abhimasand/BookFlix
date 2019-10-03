from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
    genres = models.CharField(max_length=500,default = "")
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.title

class Genres(models.Model):
    genre = models.CharField(max_length=50,default = "")

    def publish(self):
        self.save()

class Intermediate_Book(models.Model):
    user = models.ForeignKey(User,null=False,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,null=False,on_delete=models.CASCADE)
    current_page = models.CharField(max_length=10,default = "")
    status = models.CharField(max_length=200,default = "Not Read")

    def __str__(self):
        return self.book.title

class User_Book_Reading(models.Model):
    user = models.OneToOneField(User,null=False,on_delete=models.CASCADE)
    book = models.ManyToManyField("Intermediate_Book")

class User_Book_Wishlisted(models.Model):
    user = models.OneToOneField(User,null=False,on_delete=models.CASCADE)
    book = models.ManyToManyField("Intermediate_Book")

class User_Book_Currently_Reading(models.Model):
    user = models.OneToOneField(User,null=False,on_delete=models.CASCADE)
    book = models.ManyToManyField("Intermediate_Book")


