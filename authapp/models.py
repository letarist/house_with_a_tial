from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.ImageField(upload_to='personal_avatar', blank=True, verbose_name='Фотография')
    age = models.PositiveSmallIntegerField(null=True,blank=True, verbose_name='Возраст')
    address = models.CharField(max_length=150, blank=True, verbose_name='Адрес')

    def __str__(self):
        return f'{self.username}'
