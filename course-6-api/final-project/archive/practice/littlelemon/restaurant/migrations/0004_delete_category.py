# Generated by Django 4.2.6 on 2023-10-30 10:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0003_category_menu_inventory_alter_menu_price"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Category",
        ),
    ]
