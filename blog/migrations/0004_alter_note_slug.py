# Generated by Django 5.0.1 on 2024-02-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_note_count_view"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="slug",
            field=models.CharField(
                blank=True, max_length=170, null=True,
                verbose_name="транслит (слаг)"
            ),
        ),
    ]
