from django.shortcuts import render, get_object_or_404

from BookStoreApp.models import Book, Category
import random


# Create your views here.
def home(request, category_slug=None):
    category_page = None
    books = None
    if category_slug != None:
        category_page = get_object_or_404(Category, slug=category_slug)
        books = Book.objects.filter(category=category_page)
    else:
        books = Book.objects.all()

    return render(request, "home.html", dict(
        category=category_page,
        books=books
    ))


def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        try:
            book = Book.objects.get(name=searched)
            return books_detail(request, book.category.slug, book.slug)
        except Exception as ex:
            print(ex)
    return home(request)


def books_detail(request, category_slug=None, books_slug=None):
    try:
        book = Book.objects.get(category__slug=category_slug, slug=books_slug)
    except Exception as ex:
        raise ex
    return render(request, "book.html", dict(
        book=book
    ))


def about(request):
    return render(request, "about.html")
























































def check_book(name):
    try:
        x = Book.objects.get(name=name)
        return True
    except:
        pass
    return False


def check_category(name):
    try:
        x = Category.objects.get(name=name)
        return True
    except:
        pass
    return False