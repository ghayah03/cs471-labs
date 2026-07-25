from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    books = [
        {
            "title": "Python Programming",
            "author": "John Smith",
            "year": 2020
        },
        {
            "title": "Django Web Development",
            "author": "David Brown",
            "year": 2022
        },
        {
            "title": "Web Technologies",
            "author": "Mark Lee",
            "year": 2023
        }
    ]

    context = {
        "books": books
    }

    return render(request, "bookmodule/index.html", context)



def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))

def book_detail(request, book_id):
    books = [
        {
            "id": 1,
            "title": "Python Programming",
            "author": "John Smith",
            "year": 2020
        },
        {
            "id": 2,
            "title": "Django Web Development",
            "author": "David Brown",
            "year": 2022
        }
    ]

    book = None

    for b in books:
        if b["id"] == book_id:
            book = b

    context = {
        "book": book
    }

    return render(request, "bookmodule/detail.html", context)


def index(request):
    return render(request, "bookmodule/index.html")


def list_books(request):
    return render(request, "bookmodule/list_books.html")


def viewbook(request, bookId):
    return render(request, "bookmodule/one_book.html")


def aboutus(request):
    return render(request, "bookmodule/aboutus.html")


def html_links(request):
    return render(request, 'bookmodule/html_links.html')

def html_formatting(request):
    return render(request, 'bookmodule/html_formatting.html')

def html_listing(request):
    return render(request, 'bookmodule/html_listing.html')

def html_tables(request):
    return render(request, 'bookmodule/html_tables.html')





def __getBooksList():
    
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley', 'price': 45.99}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam', 'price': 39.99}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov', 'price': 29.99}
    return [book1, book2, book3]

def search(request):
    
    books = __getBooksList()  
    context = {'books': books}
    
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')  
        isAuthor = request.POST.get('option2')  
        
        newBooks = []
        for item in books:
            contained = False
            if isTitle and keyword in item['title'].lower():
                contained = True
            if not contained and isAuthor and keyword in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)
        
        context = {'books': newBooks}
    
    return render(request, 'bookmodule/search.html', context)