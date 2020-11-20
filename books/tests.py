from django.test import Client, TestCase
from django.contrib.auth import get_user_model
from .models import Book
from django.urls import reverse

# Create your tests here.

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
        Ensure the password is created right.
        """
        user_a = User.objects.get(username="sahar")
        self.assertTrue(
            user_a.check_password(self.user_a_pw)
        )


