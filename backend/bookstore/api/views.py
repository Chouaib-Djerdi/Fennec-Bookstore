from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from mainapp.models import Book
# Create your views here.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
