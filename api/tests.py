from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from .models import Book

class BookModelTestCase(TestCase):
    def setUp(self):
        self.list_create_url = reverse('book-list-create')
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            published_date='2023-08-01',
            isbn='123456789876543',
            amount=60.00,
        )
        
    def test_create_book(self):
        book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            published_date='2023-08-01',
            isbn='123456789876543',
            amount=60.00,
        )
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.author, 'Test Author')
        self.assertEqual(book.published_date, '2023-08-01')
        self.assertEqual(book.isbn, '123456789876543')
        self.assertEqual(book.amount, 60.00)

    def test_book_str_representation(self):
        book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            published_date='2023-08-01',
            isbn='123456789876543',
            amount='60.00',
        )

        self.assertEqual(str(book), 'Test Book')

class BookAPITestCase(TestCase):
    def setUp(self):
        self.list_create_url = reverse('book-list-create')
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            published_date='2023-08-01',
            isbn='123456789876543',
            amount=60.00,
        )

    def test_get_book_list(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'published_date': '2023-07-02',
            'isbn': '9876543210987',
            'amount': '50.66',
        }

        response = self.client.post(self.list_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_get_book_detail(self):
        detail_url = reverse('book-details', args=[self.book.pk])
        response = self.client.get(detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')
