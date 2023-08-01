from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from api.models import Book
from decimal import Decimal

class BookViewTests(APITestCase):
    def setUp(self):
        self.book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'published_date': '2023-08-01',
            'isbn': '1234567890',
            'amount': 19.99,
        }
        self.book = Book.objects.create(**self.book_data)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book_data['title'])
        self.assertEqual(response.data['author'], self.book_data['author'])
        self.assertEqual(response.data['published_date'], self.book_data['published_date'])
        self.assertEqual(response.data['isbn'], self.book_data['isbn'])
        self.assertEqual(Decimal(response.data['amount']), Decimal(str(self.book_data['amount'])))

    def test_create_book(self):
        url = reverse('book-create')
        response = self.client.post(url, data=self.book_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])
        self.assertEqual(response.data['author'], self.book_data['author'])
        self.assertEqual(response.data['published_date'], self.book_data['published_date'])
        self.assertEqual(response.data['isbn'], self.book_data['isbn'])
        self.assertEqual(Decimal(response.data['amount']), Decimal(str(self.book_data['amount'])))
        self.assertEqual(Book.objects.count(), 2)  

    def test_update_book(self):
        url = reverse('book-update', kwargs={'pk': self.book.pk})
        updated_data = {
            'title': 'Updated Book Title',
            'author': 'Updated Author',
            'published_date': '2023-08-02',
            'isbn': '0987654321',
            'amount': 29.99,
        }
        response = self.client.put(url, data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, updated_data['title'])

    def test_delete_book(self):
        url = reverse('book-delete', kwargs={'pk': self.book.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)  # Check if the book was deleted
