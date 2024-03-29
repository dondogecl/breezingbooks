# Generated by Django 5.0.2 on 2024-02-14 07:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Contributor",
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
                (
                    "first_names",
                    models.CharField(
                        help_text="Contributor First Names", max_length=100
                    ),
                ),
                (
                    "last_names",
                    models.CharField(
                        help_text="Contributor Last Names", max_length=100
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        help_text="Contributor Email address", max_length=254
                    ),
                ),
            ],
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
                ("title", models.CharField(help_text="Book Title", max_length=200)),
                (
                    "publication_date",
                    models.DateField(help_text="Book Publication Date"),
                ),
                ("isbn", models.CharField(help_text="Book ISBN", max_length=13)),
                (
                    "publisher",
                    models.ForeignKey(
                        help_text="Book Publisher",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reviews.publisher",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BookContributor",
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
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("AUT", "Author"),
                            ("COA", "Co-Author"),
                            ("EDT", "Editor"),
                            ("REV", "Reviewer"),
                            ("OTH", "Other"),
                        ],
                        max_length=20,
                        verbose_name="Contribution Role",
                    ),
                ),
                (
                    "book",
                    models.ForeignKey(
                        help_text="Book",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reviews.book",
                    ),
                ),
                (
                    "contributor",
                    models.ForeignKey(
                        help_text="Contributor",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reviews.contributor",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="contributors",
            field=models.ManyToManyField(
                help_text="Book Contributors",
                through="reviews.BookContributor",
                to="reviews.contributor",
            ),
        ),
        migrations.CreateModel(
            name="Review",
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
                ("content", models.TextField(help_text="Review Content")),
                ("rating", models.IntegerField(help_text="Review Rating")),
                (
                    "date_created",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Review Date Created"
                    ),
                ),
                (
                    "date_edited",
                    models.DateTimeField(help_text="Review Date Edited", null=True),
                ),
                (
                    "book",
                    models.ForeignKey(
                        help_text="Reviewed Book",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reviews.book",
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        help_text="Review Creator",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
