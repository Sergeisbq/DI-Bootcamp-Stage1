from django.urls import path
from .views import BookList, BookDetail, book_create, book_update, book_delete,book_create_post

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    # path('books/create/', BookList.as_view(), name='book-create'),
    path('books/create-post-api/', book_create_post, name='book-create-post'),
    path('books/create-post/', book_create, name='book-create'),
    path('books/update/<int:pk>/', book_update, name='book-update'),
    path('books/delete/<int:pk>/', book_delete, name='book-delete')
]