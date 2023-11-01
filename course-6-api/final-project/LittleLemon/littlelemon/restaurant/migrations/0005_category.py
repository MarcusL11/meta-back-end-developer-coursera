# Generated by Django 4.2.6 on 2023-10-30 10:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0004_delete_category"),
    ]

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
                ("slug", models.SlugField()),
                ("name", models.CharField(max_length=200)),
            ],
        ),
    ]
