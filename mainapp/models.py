from datetime import datetime

from django.db import models


class TypeOfAnimal(models.Model):
    title = models.CharField(max_length=30, verbose_name="Вид животного")
    is_active = models.BooleanField(verbose_name="Доступен", default=True)

    def __str__(self):
        return f"{self.title}"

    def delete(self, using=None, keep_parents=False):
        if self.is_active:
            self.is_active = False
        else:
            self.is_active = True
        self.save()


class Animal(models.Model):
    type = models.ForeignKey(TypeOfAnimal, on_delete=models.CASCADE, verbose_name="Вид животного")
    name = models.CharField(max_length=30, verbose_name="Имя")
    age = models.PositiveSmallIntegerField(verbose_name="Примерный возраст", blank=True)
    avatar = models.ImageField(upload_to="animal_account", verbose_name="Аватарка")
    short_description = models.CharField(max_length=70, verbose_name="Краткое описание")
    description = models.TextField(verbose_name="Описание", blank=True)
    date_entrance = models.DateTimeField(auto_created=True, verbose_name="Дата поступления", default=datetime.now())
    is_active = models.BooleanField(verbose_name="Доступен", default=True)
    taken_home = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Забрали домой",
    )

    def __str__(self):
        return f"{self.type} {self.name}"

    def delete(self, using=None, keep_parents=False):
        if self.is_active:
            self.is_active = False
        else:
            self.is_active = True
        self.save()


class Contact(models.Model):
    address = models.CharField(max_length=1000, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта")

    def __str__(self):
        return "Контакты"
