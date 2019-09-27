from django.conf import settings
from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=200)
    status = models.CharField(max_length=200,default = "Not Read")
    description = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title