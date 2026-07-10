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


