import os
import django
import sys


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libraryproject.settings')
django.setup()

from apps.bookmodule.models import Book

Book.objects.all().delete()


books = [
    {'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley', 'price': 120.00, 'edition': 3},
    {'title': 'Reversing: Secrets of Reverse Engineer', 'author': 'E. Eilam', 'price': 97.00, 'edition': 2},
    {'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov', 'price': 100.00, 'edition': 4},
]

for book_data in books:
    Book.objects.create(**book_data)

for book in Book.objects.all():
    print(f"ID: {book.id}, Title: {book.title}")

    