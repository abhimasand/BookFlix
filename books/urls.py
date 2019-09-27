from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('all_books', views.all_books, name='all_books'),
    path('about_book/<int:pk>', views.about_book, name='about_book'),
    path('about_book/<int:pk>/add_to_wishlist', views.add_to_wishlist, name='add_to_wishlist')


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


