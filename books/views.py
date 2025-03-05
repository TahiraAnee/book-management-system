from django.shortcuts import render, redirect

from .models import Book
from .forms import BookForm


def index(request):
    context = {
        "books": Book.objects.all().order_by("published_year"),
        # "books": Book.objects.all(),
    }
    return render(request, "index.html", context)


def create(request):
    if request.method == "POST":
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            return redirect("/")
    else:
        book_form = BookForm()

    context = {
        "form": book_form,
    }
    return render(request, "book_form.html", context)


def update(request, id):
    specific_book = Book.objects.get(id=id)

    if request.method == "POST":
        book_form = BookForm(request.POST, instance=specific_book)
        if book_form.is_valid():
            book_form.save()
            return redirect("/")
    else:
        book_form = BookForm(instance=specific_book)

    context = {
        "form": book_form,
    }
    return render(request, "book_form.html", context)


def delete(request, id):
    specific_book = Book.objects.get(id=id)
    specific_book.delete()
    return redirect("book_list")
