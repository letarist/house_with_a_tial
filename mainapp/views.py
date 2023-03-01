from random import sample

from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from basketapp.models import Basket

from .models import Animal, Contact, TypeOfAnimal


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


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
    context = {
        "title": "Главная",
        "all_animals": all_animals,
        "basket": basket,
        "types": types,
        "media_url": settings.MEDIA_URL,
        "get_same_animal_": get_same_animal_,
        "rand_animal": rand_animal_,
    }
    return render(request, "mainapp/index.html", context)


def contact(request):
    contacts = Contact.objects.all()
    context = {"title": "Контакты", "contacts": contacts}
    return render(request, "mainapp/contact.html", context)


def animal_of_types(request, pk=None, page=1):
    types = TypeOfAnimal.objects.all()
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    if pk:
        animal_of_type = Animal.objects.filter(type=pk).order_by("name")
        type = TypeOfAnimal.objects.get(pk=pk)
    else:
        animal_of_type = Animal.objects.all().order_by("name")
        type = {'pk': 0, 'name': 'Все'}
    paginator = Paginator(animal_of_type, 2)
    try:
        animal_paginator = paginator.page(page)
    except PageNotAnInteger:
        animal_paginator = paginator.page(1)
    except EmptyPage:
        animal_paginator = paginator.page(paginator.num_pages)
    context = {
        "type": type,
        "animal_of_type": animal_paginator,
        "basket": basket,
        "media_url": settings.MEDIA_URL,
    }
    return render(request, "mainapp/animal.html", context)


def person_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    title = animal.name
    basket = get_basket(request.user)
    context = {"animal": animal, "title": title, "basket": basket}
    return render(request, "mainapp/person_animal.html", context)
