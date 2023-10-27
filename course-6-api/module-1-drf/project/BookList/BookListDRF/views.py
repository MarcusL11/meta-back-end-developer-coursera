from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# Create your views here.

class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    

class SingleBookView(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer