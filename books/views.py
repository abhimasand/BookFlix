from django.shortcuts import render,redirect
from .models import Book, Genres
from .forms import NewUserForm

from django.core.paginator import Paginator

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import tensorflow as tf
import keras
import numpy as np
import pandas as pd
from keras.models import Model
from keras.models import model_from_json
from keras import backend as K

K.clear_session()

with open('scripts/model.json', 'r') as json_file:
    loaded_model_json = json_file.read()

loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("scripts/model.h5")
print("Loaded model from disk")
loaded_model.compile('adam', 'mean_squared_error')

genres = ['Fiction', 'Fantasy', 'Romance', 'Young Adult', 'Historical', 'Paranormal', 'Mystery', 'Nonfiction', 'Science Fiction', 
'Historical Fiction', 'Classics', 'Contemporary', 'Childrens', 'Cultural', 'Literature', 'Sequential Art', 'Thriller', 'European Literature', 
'Religion', 'History', 'Biography', 'Humor', 'Horror', 'Novels', 'Adventure', 'Crime', 'Contemporary Romance', 'Autobiography', 'Philosophy', 
'War', 'Short Stories', 'Christian', 'Paranormal Romance', 'Vampires', 'Comics', 'Womens Fiction', 'Memoir', 'Chick Lit', 'Erotica', 'Science']



class Home:
    def home(request):
        print ("**************Going to the Home Page**************")
        return render(request, 'books/home.html', {})

class Search:
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

class Find_Books:
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

class Book_Functions:
    def about_book(request,pk,status=False):
        book = Book.objects.get(pk=pk)
        return render(request, 'books/about_books.html', {'book':book})

    def add_to_wishlist(request,pk,status=False):
        book = Book.objects.get(pk=pk)
        book.status = "To Read"
        book.current_page = 0
        book.save()
        book.publish()
        print (book.pk)
        return redirect('about_book', pk=book.pk)

    def remove_from_wishlist(request,pk,status=False):
        book = Book.objects.get(pk=pk)
        book.status = "Not Read"
        book.current_page = 0
        book.save()
        book.publish()
        print (book.pk)
        return redirect('about_book', pk=book.pk)


    def currently_reading(request,pk,status=False):
        book = Book.objects.get(pk=pk)
        book.status = "Reading"
        book.save()
        book.publish()
        print (book.pk)
        return redirect('about_book', pk=book.pk)

    def change_current_page(request,pk,status="In Progress"):

        if status=="In Progress":
            book = Book.objects.get(pk=pk)
            return render(request, 'books/about_books.html', {'book':book,'flag':"In Progress"})
        else:
            book = Book.objects.get(pk=pk)
            book.current_page = request.GET.get('new_page')
            book.save()
            book.publish()
            print (book.pk)
            return redirect('about_book', pk=book.pk)

class Services:
    def services(request):
        return render(request, 'books/services.html', {})

class Registration:
    def register(request):
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f"New account created: {username}")
                login(request, user)
                return redirect("home")

            else:
                for msg in form.error_messages:
                    messages.error(request, f"{msg}: {form.error_messages[msg]}")

                return render(request = request,
                              template_name = "registration/signup.html",
                              context={"form":form})

        form = UserCreationForm
        return render(request = request,
                      template_name = "registration/signup.html",
                      context={"form":form})

    def login_request(request):
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}")
                    return redirect('home')
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()
        return render(request = request,
                        template_name = "registration/login.html",
                        context={"form":form})
    def logout_request(request):
        logout(request)
        messages.info(request, "Logged out successfully!")
        return redirect("home")



class User_Book_Data:
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

    @csrf_exempt
    def handle_selected_books(request):
        selected_books = request.POST.getlist("selected[]")
        print(selected_books)
        return HttpResponse('Success')

class Read_Books:
    def read_books(request):
        books = Book.objects.all()[:500]
        return render(request, 'books/read_books.html', {'books':books})

    def select_read_books(request):
        books = Book.objects.all()[:500]
        return render(request, 'books/read_books.html', {'books':books})

        
class Recommend_Books:
    def predictions(request):
        #get user_data
        user_data = np.array([1 for i in range(10000)])

        dataset = pd.read_csv('scripts/goodbooks-10k-master/ratings.csv')
        book_data = np.array(list(set(dataset.book_id)))
        books = pd.read_csv('scripts/goodbooks-10k-master/books.csv')

        user = np.array(user_data) #[1,1,0,1,0,0,0......0,1,1]
        predictions = loaded_model.predict([user, book_data])
        predictions = np.array([a[0] for a in predictions])
        recommended_book_ids = (-predictions).argsort()[:100]

        output = books[books['book_id'].isin(recommended_book_ids)]

        K.clear_session()

        books = Book.objects.filter(goodreads_book_id__in = list(output.goodreads_book_id))


        return render(request, 'books/all_books.html', {'books':books,'search_header':"Your Recommendations"})

    
#{% url 'sort_books_genre' request_genre=gen.genre %}










# Create your views here.
