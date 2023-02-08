from datetime import datetime

from django.db import models


class TypeOfAnimal(models.Model):
    title = models.CharField(max_length=30, verbose_name="Вид животного")

    def __str__(self):
        return f"{self.title}"


class Animal(models.Model):
    type = models.ForeignKey(TypeOfAnimal, on_delete=models.CASCADE, verbose_name="Вид животного")
    name = models.CharField(max_length=30, verbose_name="Имя")
    age = models.PositiveSmallIntegerField(verbose_name="Примерный возраст", blank=True)
    avatar = models.ImageField(upload_to="animal_account", verbose_name="Аватарка")
    short_description = models.CharField(max_length=70, verbose_name="Краткое описание")
    description = models.TextField(verbose_name="Описание", blank=True)
    date_entrance = models.DateTimeField(auto_created=True, verbose_name="Дата поступления", default=datetime.now())
    taken_home = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Забрали домой",
    )

    def __str__(self):
        return f"{self.type} {self.name}"


class Contact(models.Model):
    address = models.CharField(max_length=1000, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Почта")

    def __str__(self):
        return "Контакты"
