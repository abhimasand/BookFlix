from django.shortcuts import render,redirect
from .models import Book

def home(request):
    return render(request, 'books/home.html', {})


def all_books(request):
	books = Book.objects.all()[:300]
	return render(request, 'books/all_books.html', {'books':books})

def about_book(request,pk):
	book = Book.objects.get(pk=pk)
	return render(request, 'books/about_books.html', {'book':book})

def add_to_wishlist(request,pk):
	book = Book.objects.get(pk=pk)
	book.status = "To Read"
	book.save()
	book.publish()
	print (book.pk)
	return redirect('about_book', pk=book.pk)







# Create your views here.
