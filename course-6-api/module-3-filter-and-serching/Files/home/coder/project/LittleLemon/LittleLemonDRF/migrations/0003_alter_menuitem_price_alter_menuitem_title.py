# Generated by Django 4.2.6 on 2023-10-28 15:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("LittleLemonDRF", "0002_rename_inventroy_menuitem_inventory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name="menuitem",
            name="title",
            field=models.CharField(max_length=255),
        ),
    ]
