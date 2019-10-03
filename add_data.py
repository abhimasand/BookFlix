import csv
from books.models import Book

with open('scripts/output_with_8000_desc_genre.csv') as f:
	reader = csv.reader(f)
	print(next(reader))
	print ()
	for row in reader:
		Book.objects.create(goodreads_book_id = row[1],
			book_id = row[0],
			published_date = row[8],
			author = row[7],
			title = row[10],
			original_title = row[9],
			rating = row[12],
			description = row[23],
			image_url = row[21],
			image_location = row[24],
			genres = row[25])

		