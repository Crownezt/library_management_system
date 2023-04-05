from django.shortcuts import render
from django.views.generic import DetailView

from book.models import Book


# Create your views here.

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    context_object_name = 'post'
