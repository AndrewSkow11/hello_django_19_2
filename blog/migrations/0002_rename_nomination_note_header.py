# Generated by Django 5.0.1 on 2024-02-19 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="note",
            old_name="nomination",
            new_name="header",
        ),
    ]
