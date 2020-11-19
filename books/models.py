from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.
User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return self.title
