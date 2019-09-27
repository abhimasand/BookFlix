import csv
from books.models import Book

with open('scripts/output_with_8000_desc.csv') as f:
	reader = csv.reader(f)
	print(next(reader))
	print ()
	for row in reader:
		Book.objects.create(book_id = row[0],
			goodreads_book_id = row[1],
			published_date = row[8],
			author = row[7],
			title = row[10],
			original_title = row[9],
			rating = row[12],
			description = row[23],
			image_url = row[21],
			image_location = row[24],
			status = "Not Read",
			current_page = 0)

		