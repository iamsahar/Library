from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book

# Create your views here.

from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class BookList(APIView):
    """
    List all books, or create a new book.
    """

    def get(self, request, format=None):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(APIView):
    """
    Retrieve, update or delete a book instance.
    """

    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def books_overview(request):
#     """
#     A view that returns the URL pattern that we want to setup.
#     """
#     api_urls = {
#         'List': '/book-list/',
#         'Detail View': '/book-detail/<str:pk>/',
#         'Create': '/book-create/',
#         'Update': '/book-update/<str:pk>/',
#         'Delete': '/book-delete/<str:pk>/',
#     }
#     return Response(api_urls)
#
#
# @api_view(['GET'])
# def book_list(request):
#     """
#     A view that returns the list of books.
#     """
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def book_detail(request, pk):
#     """
#     A view that returns the detail of the created book.
#     """
#     tasks = Book.objects.get(id=pk)
#     serializer = BookSerializer(tasks, many=False)
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def book_create(request):
#     """
#     A view that creates a book.
#     """
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['POST'])
# def book_update(request, pk):
#     """
#     A view that edits a book's detail.
#     """
#     task = Book.objects.get(id=pk)
#     serializer = BookSerializer(instance=task, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def book_delete(request, pk):
#     """
#     A view that deletes a book.
#     """
#     task = Book.objects.get(id=pk)
#     task.delete()
#     return Response('Item successfully deleted!')
