from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('all_books', views.all_books, name='all_books'),
]


