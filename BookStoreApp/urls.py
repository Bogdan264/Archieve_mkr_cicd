from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("search/",  views.search, name="search"),
    path("category/<slug:category_slug>",  views.home, name="books_by_category"),
    path("category/<slug:category_slug>/<slug:books_slug>",  views.books_detail, name="books_detail"),
]
