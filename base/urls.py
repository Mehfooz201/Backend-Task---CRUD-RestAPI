
from django.urls import path
from . import views


urlpatterns = [
    # List all books and create a new book.
    path('books/', views.BooksList.as_view(), name='books'),

    # Retrieve, update, or delete a specific book by its ID.
    path('books/<int:id>', views.BooksDetails.as_view()),

]
