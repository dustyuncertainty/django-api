from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book

class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls): # Corrected name: Uppercase 'T'
        cls.book = Book.objects.create(
            title = "django for apis",
            subtitle = "build web apis with python and django",
            author = "williams s, vincent",
            isbn = "2238373737373"
        )

    def test_api_listview(self):
        # 1. Check the response status code
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # 2. Check the object count (should now be 1 due to setUpTestData)
        self.assertEqual(Book.objects.count(), 1)
        
        # 3. Check the content (You need to assert against the book's data,
        #    not the Python object itself, which will require a string or JSON key.)
        self.assertContains(response, self.book.title) # Assert against the title string
        self.assertContains(response, self.book.author)
        
        # Optional: Check the number of items returned in the JSON/list
        self.assertEqual(len(response.data), 1)