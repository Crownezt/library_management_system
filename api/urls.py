from django.urls import path, include

from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)
router.register('book_instances', views.BookInstanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('books/', views.BookListApiView.as_view(), name='home'),
    path('new_book/', views.BookCreateApiView.as_view(), name='new_book'),
    # path('book/<int:id>/', views.BookDetailApiView.as_view(), name='book_detail'),
    # path('authors/', views.AuthorListApiView.as_view(), name='author_list'),
    # path('book-authors/', views.AuthorDetailApiView.as_view(), name='author_detail'),
    path('authors/<int:pk>/', views.author_detail, name='author-detail'),
    # path('author/<int:id>/', views.AuthorDetailApiView.as_view(), name='author_detail'),
    path('new_author/', views.AuthorCreateApiView.as_view(), name='new_author'),

    # path('book/<int:pk>/', views.book_details, name='book_list'),
    # path('authors/', views.author_list, name='book_list'),
    # path('author/<int:pk>/', views.author_details, name='book_list'),
]
