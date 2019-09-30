from books.models import Genres

genres = ['Fiction', 'Fantasy', 'Romance', 'Young Adult', 'Historical', 'Paranormal', 'Mystery', 'Nonfiction', 'Science Fiction', 
'Historical Fiction', 'Classics', 'Contemporary', 'Childrens', 'Cultural', 'Literature', 'Sequential Art', 'Thriller', 'European Literature', 
'Religion', 'History', 'Biography', 'Humor', 'Horror', 'Novels', 'Adventure', 'Crime', 'Contemporary Romance', 'Autobiography', 'Philosophy', 
'War', 'Short Stories', 'Christian', 'Paranormal Romance', 'Vampires', 'Comics', 'Womens Fiction', 'Memoir', 'Chick Lit', 'Erotica', 'Science']

for x in genres:
	Genres.objects.create(genre = x)
	
