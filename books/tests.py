from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from .models import Book
from django.urls import reverse


User = get_user_model()


class UserTestCase(TestCase):

    def setUp(self):
        user_a = User(username='sahar', email='sahar@invalid.com')
        user_a_pw = "some_123_password"
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        self.user_a = user_a

    def test_user_exists(self):
        """
        Ensure we can create a user object.
        """
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        """
        Ensure the password is created correctly.
        """
        user_a = User.objects.get(username="sahar")
        self.assertTrue(
            user_a.check_password(self.user_a_pw)
        )


client = Client()


class BookTest(TestCase):

    def setUp(self, user=None):
        self.author = User.objects.create(
            username='sahar',
            email='sahar@invalid.com',
            password="some_123_password"
        )
        self.client.force_login(User.objects.get_or_create(self.author)[0])
        self.book = Book.objects.create(
            title="first title",
            author=self.author,
            publication_date="2020-11-18",
            description="good job",
        )

    def create_book(self):
        return self.book

    def test_book_creation(self):
        """
        Ensure the book is created.
        """
        b = self.create_book()
        self.assertTrue(isinstance(b, Book))
        self.assertEqual(b.__str__(), b.title)

    def test_book_list_view(self):
        """
        Ensure the book list is created correctly.
        """
        b = self.create_book()
        response = self.client.get(reverse("book_list"), authentication=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(str(b.title), str(response.content))
