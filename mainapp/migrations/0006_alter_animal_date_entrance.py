# Generated by Django 4.1.5 on 2023-02-22 13:46

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0005_typeofanimal_is_active_alter_animal_date_entrance"),
    ]

    operations = [
        migrations.AlterField(
            model_name="animal",
            name="date_entrance",
            field=models.DateTimeField(
                auto_created=True,
                default=datetime.datetime(2023, 2, 22, 16, 46, 19, 446140),
                verbose_name="Дата поступления",
            ),
        ),
    ]
