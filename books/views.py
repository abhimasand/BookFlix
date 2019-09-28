from django.shortcuts import render,redirect
from .models import Book, Genres
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView as auth_login

genres = ['Fiction', 'Fantasy', 'Romance', 'Young Adult', 'Historical', 'Paranormal', 'Mystery', 'Nonfiction', 'Science Fiction', 
'Historical Fiction', 'Classics', 'Contemporary', 'Childrens', 'Cultural', 'Literature', 'Sequential Art', 'Thriller', 'European Literature', 
'Religion', 'History', 'Biography', 'Humor', 'Horror', 'Novels', 'Adventure', 'Crime', 'Contemporary Romance', 'Autobiography', 'Philosophy', 
'War', 'Short Stories', 'Christian', 'Paranormal Romance', 'Vampires', 'Comics', 'Womens Fiction', 'Memoir', 'Chick Lit', 'Erotica', 'Science']

def home(request):
    return render(request, 'books/home.html', {})

def search_books(request):
    return render(request, 'books/search.html', {})

def search(request):
    query = request.GET.get('search_value')
    book_list = Book.objects.filter(title__contains=query)
    genres = Genres.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, 1000)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'books/all_books.html', {'books':books,'genres':genres,'focus_genre':"False",'search_header':f"Search Results For: {query}"})

def all_books(request):
    book_list = Book.objects.all()
    genres = Genres.objects.all()
    
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, 1000)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'books/all_books.html', {'books':books,'genres':genres,'focus_genre':"False"})

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

def currently_reading(request,pk):
    book = Book.objects.get(pk=pk)
    book.status = "Reading"
    book.save()
    book.publish()
    print (book.pk)
    return redirect('about_book', pk=book.pk)

def set_currently_reading_page(request,page,pk):
    book = Book.objects.get(pk=pk)
    book.current_page = page
    book.save()
    book.publish()
    print (book.pk)
    return redirect('about_book', pk=book.pk)

def services(request):
    return render(request, 'books/services.html', {})

def login(request):
    if request.user.is_author():
        return redirect('/')
    elif request.user.is_reader():
        return redirect('/')

    defaults = {
        'authentication_form': CustomAuthenticationForm,
        'template_name': 'core/login.html',
    }

    return auth_login(request, **defaults)

def sort_books_genre(request,request_genre):
    if request_genre in genres:
        book_list = Book.objects.filter(genres__contains=request_genre)
        genre = Genres.objects.all()

        page = request.GET.get('page', 1)

        paginator = Paginator(book_list, 1000)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)

        return render(request, 'books/all_books.html', {'books':books,'genres':genre,'focus_genre':request_genre})
    else:
        return redirect('all_books')

def select_user_preferences(request):
    book_list = Book.objects.all()
    
    page = request.GET.get('page', 1)

    paginator = Paginator(book_list, 1000)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'books/user_select_books.html', {"books":books})

#{% url 'sort_books_genre' request_genre=gen.genre %}










# Create your views here.
