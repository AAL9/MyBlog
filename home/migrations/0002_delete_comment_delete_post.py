# Generated by Django 4.2.2 on 2023-06-20 09:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Comment",
        ),
        migrations.DeleteModel(
            name="Post",
        ),
    ]