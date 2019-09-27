from django.shortcuts import render,redirect
from .models import Book
from django.core.paginator import Paginator


def home(request):
    return render(request, 'books/home.html', {})


def all_books(request):
    book_list = Book.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, 1000)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

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

def services(request):
    return render(request, 'books/services.html', {})








# Create your views here.
