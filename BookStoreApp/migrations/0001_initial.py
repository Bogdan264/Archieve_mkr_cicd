# Generated by Django 4.2.1 on 2023-06-02 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, unique=True)),
                ("slug", models.SlugField(max_length=250, unique=True)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250, unique=True)),
                ("slug", models.SlugField(max_length=250, unique=True)),
                ("description", models.TextField(blank=True)),
                ("image", models.TextField()),
                ("link_to_book", models.TextField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="BookStoreApp.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "book",
                "verbose_name_plural": "books",
                "ordering": ("name",),
            },
        ),
    ]
