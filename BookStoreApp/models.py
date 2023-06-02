from django.urls import reverse

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_url(self):
        return reverse("books_by_category", args=[self.slug])

    def str(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #image = models.ImageField(upload_to='book', blank=True)
    image = models.TextField()
    link_to_book = models.TextField()

    class Meta:
        ordering = ("name",)
        verbose_name = "book"
        verbose_name_plural = "books"

    def get_url(self):
        return reverse("books_detail", args=[self.category.slug, self.slug])

    def str(self):
        return self.name
