# Generated by Django 4.2.1 on 2023-11-04 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("achievements", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="achievement",
            name="level",
        ),
    ]