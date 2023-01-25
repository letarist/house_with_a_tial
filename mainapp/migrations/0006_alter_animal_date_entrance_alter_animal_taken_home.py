# Generated by Django 4.1.5 on 2023-01-25 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_alter_animal_date_entrance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='date_entrance',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2023, 1, 25, 22, 9, 32, 550136), verbose_name='Дата поступления'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='taken_home',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Забрали домой'),
        ),
    ]
