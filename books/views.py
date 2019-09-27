from django.shortcuts import render

def home(request):
    return render(request, 'books/home.html', {})


def all_books(request):
    return render(request, 'books/all_books.html', {})


# Create your views here.
