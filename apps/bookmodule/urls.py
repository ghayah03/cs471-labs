from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('book/<int:bookid>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    
    path('html5/links/', views.html_links, name="books.html_links"),
    path('html5/text/formatting/', views.html_formatting, name="books.html_formatting"),
    path('html5/listing/', views.html_listing, name="books.html_listing"),
    path('html5/tables/', views.html_tables, name="books.html_tables"),
    path('search/', views.search, name="books.search"),
    path('simple/query/', views.simple_query, name="books.simple_query"),
    path('complex/query/', views.complex_query, name="books.complex_query"),
]