# Generated by Django 5.0.1 on 2024-03-05 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_version"),
    ]

    operations = [
        migrations.AlterField(
            model_name="version",
            name="is_current",
            field=models.BooleanField(default=True, verbose_name="текущая"),
        ),
    ]
