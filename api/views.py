from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.viewsets import ModelViewSet
from django.core.mail import send_mail
from api.pagination import DefaultPageNumberPagination
from api.permissions import IsAdminOrReadOnly
from api.serializers import BookSerializer, BookCreateSerializer, AuthorSerializer, AuthorCreateSerializer, \
    BookInstanceSerializer
from book.models import Book, Author, BookInstance

from rest_framework import generics, status


# Create your views here.
# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.select_related('author').all()
#     serializer_class = BookSerializer


class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer


# class AuthorListApiView(generics.ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class AuthorDetailApiView(generics.RetrieveAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     lookup_field = 'id'


class AuthorCreateApiView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorCreateSerializer


# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'id'


class AuthorViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPagination
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@api_view()
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    message = 'Smile, you are rude, very very rude'
    subject = 'Smile must offer django'
    send_mail(subject, message, 'adepheranmie@gmail.com', 'helloadewunmi@gmail.com')
    return Response(serializer.data)

# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == "GET":
#         queryset = Book.objects.all()
#         serializers = BookSerializer(queryset, many=True)
#         return Response(serializers.data)
#     elif request.method == "POST":
#         book = BookCreateSerializer(data=request.data)
#         book.is_valid(raise_exception=True)
#         book.save()
#         return Response("book saved successfully")


#
# @api_view(['GET', 'DELETE', 'PATCH', 'DELETE'])
# def book_details(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#
#     if request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET'])
# def author_list(request):
#
#     if request.method == "GET":
#         queryset = Author.objects.all()
#         serializers = AuthorSerializer(queryset, many=True)
#         return Response(serializers.data)
#
#
# @api_view(['GET'])
# def author_details(request, pk):
#
#     if request.method == "GET":
#         queryset = Author.objects.get(pk=pk)
#         serializers = AuthorSerializer(queryset)
#         return Response(serializers.data)


class BookInstanceViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPagination
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer

