from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
# Create your views here.

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


@csrf_exempt
def book_create_post(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Book created successfully.'}, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)

def book_create(request):
    if request.method == 'POST':
        serializer = BookSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('book-list')
    else:
        serializer = BookSerializer
    return render(request, 'book_create.html', {'serializer': serializer})


def book_update(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        serializer = BookSerializer(instance=book, data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('book-list')
    else:
        serializer = BookSerializer(instance=book)
    return render(request, 'book_update.html', {'serializer': serializer, 'book': book})

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book-list')
    return render(request, 'book_delete.html', {'book': book})