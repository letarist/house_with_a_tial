import random

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now
from datetime import timedelta



class User(AbstractUser):
    avatar = models.ImageField(upload_to="personal_avatar", blank=True, verbose_name="Фотография")
    age = models.PositiveSmallIntegerField(null=True, blank=True, verbose_name="Возраст")
    address = models.CharField(max_length=150, blank=True, verbose_name="Адрес")
    activate_key = models.CharField(verbose_name='Ключ активации', max_length=128, blank=True)
    activation_key_expired = models.DateTimeField(verbose_name='Актуальность ключа',
                                                  default=now() + timedelta(hours=48))

    def __str__(self):
        return f"{self.username}"

    def is_user_activation_key_expired(self):
        if now() > self.activation_key_expired:
            return False
        else:
            return True

    def delete(self, using=None, keep_parents=False):
        if self.is_active:
            self.is_active = False
        else:
            self.is_active = True
        self.save()


