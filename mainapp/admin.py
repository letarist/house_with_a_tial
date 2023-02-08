from django.contrib import admin

from .models import Animal, TypeOfAnimal

admin.site.register(TypeOfAnimal)
admin.site.register(Animal)
