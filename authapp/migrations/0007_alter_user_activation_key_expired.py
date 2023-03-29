# Generated by Django 4.1.5 on 2023-03-22 18:03

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0006_alter_user_activation_key_expired"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="activation_key_expired",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 3, 24, 18, 3, 11, 411882, tzinfo=datetime.timezone.utc),
                verbose_name="Актуальность ключа",
            ),
        ),
    ]
