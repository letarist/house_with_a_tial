from django.shortcuts import render
from django.conf import settings
from .models import Animal, TypeOfAnimal, Contact


def index(request):
    types = TypeOfAnimal.objects.all()
    all_animals = Animal.objects.all()
    context = {'title': 'Главная', "all_animals": all_animals, "types": types, 'media_url': settings.MEDIA_URL}
    return render(request, 'mainapp/index.html', context)


def contact(request):
    contacts = Contact.objects.all()
    context = {"title": "Контакты", "contacts": contacts}
    return render(request, 'mainapp/contact.html', context)


def animal_of_types(request, pk=None):
    types = TypeOfAnimal.objects.all()
    if pk:
        animal_of_type = Animal.objects.filter(type=pk)
    else:
        animal_of_type = Animal.objects.all()
    context = {'types': types, 'animal_of_type': animal_of_type, 'media_url': settings.MEDIA_URL}
    return render(request, 'mainapp/animal.html', context)
