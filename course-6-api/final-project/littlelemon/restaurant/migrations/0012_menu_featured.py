# Generated by Django 4.2.7 on 2023-11-10 07:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0011_alter_menu_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="menu",
            name="featured",
            field=models.BooleanField(default=False),
        ),
    ]
