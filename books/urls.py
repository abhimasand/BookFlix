from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .forms import CustomAuthenticationForm

urlpatterns = [
    path('', views.home, name='home'),
    path('all_books', views.all_books, name='all_books'),
    path('all_books/<request_genre>', views.sort_books_genre, name='sort_books_genre'),
    path('all_books/select_user_preferences', views.select_user_preferences, name='select_user_preferences'),
    path('about_book/<int:pk>', views.about_book, name='about_book'),
    path('about_book/<int:pk>/add_to_wishlist', views.add_to_wishlist, name='add_to_wishlist'),
    path('about_book/<int:pk>/currently_reading', views.currently_reading, name='currently_reading'),
    path('services', views.services, name='services'),
    path('search_books', views.search_books, name='search_books'),
    path('search_books/search', views.search, name='search'),

    url( r'^login/$',auth_views.LoginView.as_view(template_name="books/login.html"), name="login"),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


