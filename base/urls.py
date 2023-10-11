
from django.urls import path
from . import views


urlpatterns = [
    path('books/', views.BooksList.as_view(), name='books'),

    path('books/<int:id>', views.BooksDetails.as_view()),

]
