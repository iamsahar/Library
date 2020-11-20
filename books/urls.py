from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name="book_list"),
    path('books/<int:pk>/', views.BookDetail.as_view(), name="book_detail"),
    # path('', views.books_overview, name="books_overview"),
    # path('book_list/', views.book_list, name="book_list"),
    # path('book_detail/<str:pk>/', views.book_detail, name="book_detail"),
    # path('book_create/', views.book_create, name="book_create"),
    # path('book_update/<str:pk>/', views.book_update, name="book_update"),
    # path('book_delete/<str:pk>/', views.book_delete, name="book_delete"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
