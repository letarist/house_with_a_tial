from django.conf import settings
from django.shortcuts import render, get_object_or_404
from random import sample

from .models import Animal, Contact, TypeOfAnimal
from basketapp.models import Basket


def rand_animal():
    hot_animal = Animal.objects.all()
    return sample(list(hot_animal), 1)[0]


def get_same_animal(rand_animal_):
    animals_category_rand_animal = Animal.objects.filter(type=rand_animal_.type).exclude(pk=rand_animal_.pk)[:2]
    return animals_category_rand_animal


def index(request):
    types = TypeOfAnimal.objects.all()
    all_animals = Animal.objects.all()
    rand_animal_ = rand_animal()
    get_same_animal_ = get_same_animal(rand_animal_)

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {"title": "Главная", "all_animals": all_animals, 'basket': basket, "types": types,
               "media_url": settings.MEDIA_URL, 'get_same_animal_': get_same_animal_,
               'rand_animal': rand_animal_}
    return render(request, "mainapp/index.html", context)


def contact(request):
    contacts = Contact.objects.all()
    context = {"title": "Контакты", "contacts": contacts}
    return render(request, "mainapp/contact.html", context)


def animal_of_types(request, pk=None):
    types = TypeOfAnimal.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    if pk:
        animal_of_type = Animal.objects.filter(type=pk).order_by("name")
        title = TypeOfAnimal.objects.get(pk=pk)
    elif pk == 0:
        animal_of_type = Animal.objects.all().order_by('name')
        title = 'Все'
    else:
        animal_of_type = Animal.objects.all()
        title = 'Все'
    context = {"types": types, "animal_of_type": animal_of_type, 'basket': basket, "media_url": settings.MEDIA_URL,
               'title': title}
    return render(request, "mainapp/animal.html", context)


def person_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    title = animal.name
    context = {
        'animal': animal,
        'title': title
    }
    return render(request, 'mainapp/person_animal.html', context)
