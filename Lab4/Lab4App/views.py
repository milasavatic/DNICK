from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
from datetime import datetime


# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {'books_list': books, 'app_name': 'Lab4App'}
    return render(request, 'index.html', context)


def details(request, book_id):
    book = Book.objects.filter(id=book_id).first()
    context = {'book_data': book, 'app_name': 'Lab4App'}
    return render(request, 'details.html', context)


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')

    form = BookForm()
    return render(request, "add.html", context={'form': form})
