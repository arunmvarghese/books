from django.urls import path
from .views import BookListCreateView, BookRetrieveView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('api/books/', BookListCreateView.as_view(), name='book-list'),
    path('api/books/create/', BookCreateView.as_view(), name='book-create'),
    path('api/books/<int:pk>/', BookRetrieveView.as_view(), name='book-detail'),
    path('api/books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('api/books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]

