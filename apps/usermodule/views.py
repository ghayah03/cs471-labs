from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.GET.get("name") or "world!"
    return render(request, "bookmodule/index.html", {"name": name})

def list_books(request):
    books = [
        {'id': 1, 'title': 'Internet & World Wide Web How to Program', 'author': 'Deitel'},
        {'id': 2, 'title': 'C++ How to Program', 'author': 'Deitel'},
        {'id': 3, 'title': 'Python Crash Course', 'author': 'Matthes'},
    ]
    return render(request, 'bookmodule/list_books.html', {'books': books})

def viewbook(request, bookId):
    books = {
        1: {'id': 1, 'title': 'Internet & World Wide Web How to Program', 'author': 'Deitel', 'description': 'A comprehensive introduction to web programming.'},
        2: {'id': 2, 'title': 'C++ How to Program', 'author': 'Deitel', 'description': 'A comprehensive introduction to C++ programming.'},
        3: {'id': 3, 'title': 'Python Crash Course', 'author': 'Matthes', 'description': 'A hands-on, project-based introduction to Python.'},
    }
    book = books.get(bookId)
    return render(request, 'bookmodule/one_book.html', {'book': book})

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')


def html_links(request):
    return render(request, 'bookmodule/html_links.html')

def html_formatting(request):
    return render(request, 'bookmodule/html_formatting.html')

def html_listing(request):
    return render(request, 'bookmodule/html_listing.html')

def html_tables(request):
    return render(request, 'bookmodule/html_tables.html')