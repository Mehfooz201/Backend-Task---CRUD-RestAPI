from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import OnlineBookStore
from .serializer import BookStoreSerailizer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
def home(request):
    return HttpResponse('Hey, Its API work ehre')


# ----------------------- Making API Endpoints here --------------------------

#Books List
class BooksList(APIView):
    def get(self, request):
        books = OnlineBookStore.objects.all()
        serializers = BookStoreSerailizer(books, many=True)
        return Response(serializers.data)
    
    def post(self, request):
        serializers = BookStoreSerailizer(data=request.data)
        serializers.is_valid()
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)


#Each Books Details
class BooksDetails(APIView):
    def get(self, request, id):
        books = get_object_or_404(OnlineBookStore, pk=id)
        serializers = BookStoreSerailizer(books)
        return Response(serializers.data)

    def put(self, request, id):
        books = get_object_or_404(OnlineBookStore, pk=id)
        serializers = BookStoreSerailizer(instance=books, data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data)

    def delete(self, request, id):
        books = get_object_or_404(OnlineBookStore, pk=id)
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
