from django.conf import settings
from django.db import models

from mainapp.models import Animal


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Чья корзина")
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Кого забирают")
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name="Сколько животных")
    add_time = models.DateTimeField(verbose_name="Когда забрали", auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.animal}"

    @property
    def total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        full_quantity = sum(list(map(lambda x: x.quantity, _items)))
        return full_quantity
