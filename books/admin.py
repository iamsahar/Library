from django.contrib import admin
from .models import Book

# Register your models here.


# class BookAdmin(admin.ModelAdmin):
#     fields = [
#         'title',
#         'author',
#         'publication_date',
#         'description',
#     ]
#
#     class Meta:
#         model = Book

admin.site.register(Book) #, BookAdmin