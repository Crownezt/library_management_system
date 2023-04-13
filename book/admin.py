from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from book.models import Book, Author, BookInstance, LibraryUser


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'isbn', 'genre', 'language', 'price']
    list_editable = ['price']
    list_per_page = 10
    list_filter = ['title']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth']
    list_per_page = 10


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['unique_id', 'due_back', 'status', 'book', 'imprint', 'borrower']


# admin.site.register(Genre)
# admin.site.register(Language)
