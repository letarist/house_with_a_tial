from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.ImageField(upload_to="personal_avatar", blank=True, verbose_name="Фотография")
    age = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Возраст")
    address = models.CharField(max_length=150, blank=True, verbose_name="Адрес")
    is_active = models.BooleanField(verbose_name='Заблокировани/не заблокировани', default=True)

    def __str__(self):
        return f"{self.username}"
