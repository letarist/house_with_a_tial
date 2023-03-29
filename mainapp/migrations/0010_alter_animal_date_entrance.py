# Generated by Django 4.1.5 on 2023-03-19 12:02

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0009_alter_animal_date_entrance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="date_entrance",
            field=models.DateTimeField(
                auto_created=True,
                default=datetime.datetime(2023, 3, 19, 15, 2, 53, 739605),
                verbose_name="Дата поступления",
            ),
        ),
    ]
