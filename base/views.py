from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import OnlineBookStore
from .serializer import BookStoreSerailizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.


def home(request):
    """
    A simple view that returns a greeting message.
    """
    return HttpResponse("Hey, It's an API work here")




# API Endpoints for BookStore

class BooksList(APIView):
    """
    Provides a list of books or allows creating a new book.
    """
    
    def get(self, request):
        """
        Retrieve a list of all books.
        """
        #Fetching all the records from model class database.
        books = OnlineBookStore.objects.all()

        #responsible for serializing data (converting complex data types into JSON Format for API)
        #many=True => Because we are fetching multiple books record
        serializer = BookStoreSerailizer(books, many=True) 

        #Return the serialized book data in an API response.
        return Response(serializer.data)
    

    def post(self, request):
        """
        Create a new book.
        """
        # Create a new serializer instance with the data from the request.
        serializer = BookStoreSerailizer(data=request.data)

        # Check if the data provided in the request is valid according to the serializer's defined validation rules.
        serializer.is_valid()

        # Save the valid data, creating a new BookStore instance in the database.
        serializer.save()

        # Return a response containing the serialized data of the newly created object
        # and a status code indicating successful creation (HTTP 201 - Created).
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BooksDetails(APIView):
    """
    Provides details of a specific book, allows updating, or deleting it.
    """
    
    def get(self, request, id):
        """
        Retrieve details of a specific book by its ID.
        """
        # Retrieve a specific book by its ID (primary key).
        book = get_object_or_404(OnlineBookStore, pk=id)

        # Serialize the book data.
        serializer = BookStoreSerailizer(book)

        # Return the serialized book data in an API response.
        return Response(serializer.data)


    def put(self, request, id):
        """
        Update details of a specific book by its ID.
        """
        # Retrieve a specific book by its ID (primary key).
        book = get_object_or_404(OnlineBookStore, pk=id)

        # Create a serializer for the book with updated data.
        serializer = BookStoreSerailizer(instance=book, data=request.data)

        # Check if the updated data is valid, and raise an exception if not.
        serializer.is_valid(raise_exception=True)

        # Save the updated book data to the database.
        serializer.save()

        # Return the serialized updated book data in an API response.
        return Response(serializer.data)


    def delete(self, request, id):
        """
        Delete a specific book by its ID.
        """
        # Retrieve a specific book by its ID (primary key).
        book = get_object_or_404(OnlineBookStore, pk=id)

        # Delete the specified book from the database.
        book.delete()

        # Return an API response indicating a successful deletion (HTTP 204 - No Content).
        return Response(status=status.HTTP_204_NO_CONTENT)

