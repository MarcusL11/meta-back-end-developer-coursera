# Generated by Django 4.2.6 on 2023-10-30 10:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0002_menu_menu_item_description"),
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
        migrations.AddField(
            model_name="menu",
            name="inventory",
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="menu",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
