from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from authapp.forms import UserRegisterForm
from authapp.models import User
from mainapp.models import Animal, TypeOfAnimal

from .forms import CreateAnimal, CreateType, EditAnimal


@user_passes_test(lambda u: u.is_superuser)
def add_type(request):
    if request.method == "POST":
        create_type = CreateType(request.POST, request.FILES)
        if create_type.is_valid():
            create_type.save()
            return HttpResponseRedirect(reverse("adminapp:show_animal", args=[0]))
    create_type = CreateType()
    context = {"create_type": create_type}
    return render(request, "adminapp/create_type.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_type(request, pk):
    delete_type = get_object_or_404(TypeOfAnimal, pk=pk)
    if delete_type.is_active:
        delete_type.is_active = False
        delete_type.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@user_passes_test(lambda u: u.is_superuser)
def edit_type(request, pk):
    type_animal = get_object_or_404(TypeOfAnimal, pk=pk)
    if request.method == "POST":
        edit_type = CreateType(request.POST, request.FILES, instance=type_animal)
        if edit_type.is_valid():
            edit_type.save()
            return HttpResponseRedirect(reverse("adminapp:show_animal", args=[0]))
    edit_type = CreateType(instance=type_animal)
    context = {
        "edit_type": edit_type,
    }
    return render(request, "adminapp/edit_type.html", context)


@user_passes_test(lambda u: u.is_superuser)
def add_animal(request):
    if request.method == "POST":
        create_form = CreateAnimal(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()
            return HttpResponseRedirect(reverse("adminapp:show_animal", args=[0]))
    create_form = CreateAnimal()
    context = {"create_form": create_form}
    return render(request, "adminapp/create_animal.html", context)


@user_passes_test(lambda u: u.is_superuser)
def edit_animal(request, pk):
    current_animal = get_object_or_404(Animal, pk=pk)
    if request.method == "POST":
        edit_form = EditAnimal(request.POST, request.FILES, instance=current_animal)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("adminapp:show_animal", args=[current_animal.type.pk]))
    edit_form = EditAnimal(instance=current_animal)
    context = {"edit_form": edit_form}
    return render(request, "adminapp/edit_animal.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if animal.is_active:
        animal.is_active = False
        animal.save()
    return HttpResponseRedirect(reverse("adminapp:show_animal", args=[animal.type.pk]))


@user_passes_test(lambda u: u.is_superuser)
def show_animal(request, pk):
    animal_types = TypeOfAnimal.objects.all()
    if pk != 0:
        animals_of_type = Animal.objects.filter(type=pk).order_by("name")

    else:
        animals_of_type = Animal.objects.all()
        context = {
            "animals_of_type": animals_of_type,
            "animal_types": animal_types,
        }
        return render(request, "adminapp/show_all_animals.html", context)
    type_of_animal = get_object_or_404(TypeOfAnimal, pk=pk)
    context = {
        "animals_of_type": animals_of_type,
        "animal_types": animal_types,
        "type_of_animal": type_of_animal,
    }
    return render(request, "adminapp/main_admin.html", context)


@user_passes_test(lambda u: u.is_superuser)
def detail_animal(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    animal_types = TypeOfAnimal.objects.all()
    context = {
        "animal": animal,
        "animal_types": animal_types,
    }
    return render(request, "adminapp/detail_animal.html", context)


@user_passes_test(lambda u: u.is_superuser)
def add_user(request):
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST, request.FILES)
        if user_form.is_valid():
            user_form.save()
            return HttpResponseRedirect(reverse("adminapp:show_users"))
    else:
        user_form = UserRegisterForm()
    context = {
        "user_form": user_form,
    }
    return render(request, "adminapp/add_user.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.is_active:
        user.is_active = False
        user.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


@user_passes_test(lambda u: u.is_superuser)
def show_users(request):
    users = User.objects.all().order_by("-is_active", "username")
    context = {
        "users": users,
    }
    return render(request, "adminapp/show_users.html", context)
