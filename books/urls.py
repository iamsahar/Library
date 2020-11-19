from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_overview, name="books_overview"),
    path('book_list/', views.book_list, name="book_list"),
    path('book_detail/<str:pk>/', views.book_detail, name="book_detail"),
]
