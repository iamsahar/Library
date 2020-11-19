from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book


# Create your views here.

@api_view(['GET'])
def books_overview(request):
    """
    A view that returns the URL pattern that we want to setup.
    """
    api_urls = {
        'List': '/book-list/',
        'Detail View': '/book-detail/<str:pk>/',
        'Create': '/book-create/',
        'Update': '/book-update/<str:pk>/',
        'Delete': '/book-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def book_list(request):
    """
    A view that returns the list of books.
    """
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def book_detail(request, pk):
    """
    A view that returns the detail of the created book.
    """
    tasks = Book.objects.get(id=pk)
    serializer = BookSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def book_create(request):
    """
    A view that creates a book.
    """
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def book_update(request, pk):
    """
    A view that edits a book's detail.
    """
    task = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def book_delete(request, pk):
    """
    A view that deletes a book.
    """
    task = Book.objects.get(id=pk)
    task.delete()
    return Response('Item successfully deleted!')
