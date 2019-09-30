from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from django.conf.urls import url
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.Home.home, name='home'),

    path('all_books', views.Find_Books.all_books, name='all_books'),
    path('all_books/<request_genre>', views.Find_Books.sort_books_genre, name='sort_books_genre'),

    path('all_books/select_user_preferences', views.User_Book_Data.select_user_preferences, name='select_user_preferences'),
    
    path('about_book/<int:pk>', views.Book_Functions.about_book, name='about_book'),
    path('about_book/<int:pk>/add_to_wishlist', views.Book_Functions.add_to_wishlist, name='add_to_wishlist'),
    path('about_book/<int:pk>/remove_from_wishlist', views.Book_Functions.remove_from_wishlist, name='remove_from_wishlist'),
    path('about_book/<int:pk>/currently_reading', views.Book_Functions.currently_reading, name='currently_reading'),
    path('about_book/<int:pk>/<status>/currently_reading/change_current_page', views.Book_Functions.change_current_page, name='change_current_page'),

    path('services', views.Services.services, name='services'),

    path('search_books', views.Search.search_books, name='search_books'),
    path('search_books/search', views.Search.search, name='search'),

    path('read_books', views.Read_Books.read_books, name='read_books'),
    path('read_books/select', views.Read_Books.select_read_books, name='select_read_books'),

    path('read_books/handle_selected_books', views.User_Book_Data.handle_selected_books, name='handle_selected_books'),
    path('predictions', views.Recommend_Books.predictions, name='predictions'),


    path("login/", views.Registration.login_request, name="login"),
    path("register/", views.Registration.register, name="register"),
    path("logout/", views.Registration.logout_request, name="logout"),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


