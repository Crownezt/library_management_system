from enum import Enum
from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.datetime_safe import datetime


# Create your models here.

class LibraryUser(AbstractUser):
    email = models.EmailField(unique=True)


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(default='', blank=True, null='False')
    date_of_birth = models.DateField(blank=False, null=False)
    date_of_death = models.DateField(blank=True, null=True, default='0000-00-00')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    GENRE_CHOICE = [
        ('FINANCE', 'FIN'),
        ('POLITICS', 'POL'),
        ('POWER', 'POW'),
        ('COMEDY', 'COM')
    ]

    LANGUAGE_CHOICE = [
        ('YORUBA', 'YOR'),
        ('IGBO', 'IGB'),
        ('HAUSA', 'HAU'),
        ('ENGLISH', 'ENG')
    ]

    title = models.CharField(max_length=225, blank=False, null=False)
    isbn = models.CharField(max_length=13, blank=False, null=False)
    description = models.CharField(max_length=200, blank=False, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=13, choices=GENRE_CHOICE, default='FIN')
    language = models.CharField(max_length=13, choices=LANGUAGE_CHOICE, default='YOR')
    price = models.DecimalField(default=0, max_digits=6, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title

# class Genre(models.Model):
#     GENRE_CHOICES = [
#         ('ROMANCE', 'ROM'),
#         ('THRILLER', 'THR'),
#         ('FICTION', 'FIC'),
#         ('DRAMA', 'DRA')
#     ]
#     name = models.CharField(max_length=10, choices=GENRE_CHOICES, default='ROM')
#
#     def __str__(self):
#         return self.name


# class Language(models.Model):
#     LANGUAGE_CHOICES = [
#         ('ENGLISH', 'ENG'),
#         ('FRENCH', 'FRE'),
#         ('SPANISH', 'SPA'),
#         ('ARABIC', 'ARA')
#     ]
#     name = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='ENG')
#
#     def __str__(self):
#         return self.name


class BookInstance(models.Model):
    STATUS_CHOICES = [
        ('AVAILABLE', 'AV'),
        ('BORROWED', 'BR')
    ]
    unique_id = models.UUIDField(primary_key=True, default=uuid4)
    due_back = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='A')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    imprint = models.CharField(max_length=55)
    borrower = models.OneToOneField(LibraryUser, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.imprint

# class BookInstance(models.Model):
#     unique_id = models.CharField(max_length=15)
#     due_back = models.DateField()
#
#     class LoanStatus(models.TextChoices):
#         AVAILABLE = "AVAILABLE"
#         BORROWED = "BORROWED"
#     status = models.CharField(max_length=15, choices=LoanStatus.choices)
#     imprint = models.CharField(max_length=225)
#     borrower = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='borrower')
