# Generated by Django 4.1 on 2022-08-26 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
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
                ("content", models.CharField(max_length=255)),
                ("created_date", models.DateTimeField(auto_now_add=True, null=True)),
                ("deadline", models.DateTimeField(blank=True, null=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True,
                        default=None,
                        null=True,
                        related_name="tags",
                        to="app.tag",
                    ),
                ),
            ],
            options={
                "ordering": ("status",),
            },
        ),
    ]
