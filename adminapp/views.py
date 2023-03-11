from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse

from authapp.forms import UserRegisterForm
from authapp.models import User
from mainapp.models import Animal, TypeOfAnimal

from .forms import CreateAnimal, CreateType, EditAnimal


class CreateType(LoginRequiredMixin, CreateView):
    model = TypeOfAnimal
    template_name = 'adminapp/create_type.html'
    fields = '__all__'
    success_url = reverse_lazy('adminapp:show_animal', args=[0])

    def test_func(self):
        if self.request.user.is_superuser:
            return self.request.user


class DetailAnimal(LoginRequiredMixin, DetailView):
    model = Animal
    template_name = 'adminapp/detail_animal.html'


class DeleteType(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = TypeOfAnimal
    template_name = 'adminapp/delete_type.html'
    success_url = reverse_lazy('adminapp:show_animal', args=[0])

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        if self.request.user.is_superuser:
            return self.request.user


<<<<<<< HEAD
class EditType(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = TypeOfAnimal
    template_name = 'adminapp/edit_type.html'
    fields = '__all__'
    success_url = reverse_lazy('adminapp:show_animal', args=[0])

    def test_func(self):
        return self.request.user.is_superuser


class AddAnimal(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = Animal
    template_name = 'adminapp/create_animal.html'
    success_url = reverse_lazy('adminapp:show_animal', args=[0])
    fields = ('name', 'age', 'short_description', 'description', 'type')

    def get_initial(self):
        return {'type': self.kwargs['pk']}

    def test_func(self):
        if self.request.user.is_superuser:
            return self.request.user


class EditAnimal(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Animal
    template_name = 'adminapp/edit_animal.html'
    fields = '__all__'
    success_url = reverse_lazy('adminapp:show_animal', args=[0])

    def test_func(self):
        return self.request.user.is_superuser
=======
@user_passes_test(lambda u: u.is_superuser)
def edit_type(request, pk):
    type_animal = get_object_or_404(TypeOfAnimal, pk=pk)
    if request.method == "POST":
        edit_type = CreateType(request.POST, request.FILES, instance=type_animal)
        if edit_type.is_valid():
            edit_type.save()
            return HttpResponseRedirect(reverse("adminapp:show_animal", args=[pk]))
    edit_type = CreateType(instance=type_animal)
    context = {
        "edit_type": edit_type,
    }
    return render(request, "adminapp/edit_type.html", context)


@user_passes_test(lambda u: u.is_superuser)
def add_animal(request, pk):
    type_animal = get_object_or_404(TypeOfAnimal, pk=pk)
    if request.method == "POST":
        create_form = CreateAnimal(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()
            return HttpResponseRedirect(reverse("adminapp:show_animal", args=[pk]))
    else:
        create_form = CreateAnimal(initial={'type': type_animal})
    context = {"create_form": create_form, 'type_animal': type_animal}
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
>>>>>>> main


class DeleteAnimal(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Animal
    template_name = 'adminapp/delete_animal.html'
    success_url = reverse_lazy('adminapp:show_animal', args=[0])

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return self.request.user.is_superuser


<<<<<<< HEAD
class ShowAnimal(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model = Animal
    template_name = 'adminapp/show_all_animals.html'

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(ShowAnimal, self).get_context_data(**kwargs)
        data['animal_types'] = TypeOfAnimal.objects.all()
        if self.kwargs['pk'] != 0:
            object_list = Animal.objects.filter(type=self.kwargs['pk'])
            data['object_list'] = object_list
        return data


class AddUser(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    model = User
    template_name = 'adminapp/add_user.html'
    fields = ('username', 'password', 'email', 'avatar')
    success_url = reverse_lazy('adminapp:show_animal', args=[0])

    def test_func(self):
        return self.request.user.is_superuser
=======
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
>>>>>>> main


class DeleteUser(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'adminapp/delete_user.html'
    success_url = reverse_lazy('adminapp:show_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        return self.request.user.is_superuser


<<<<<<< HEAD
class ShowUsers(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'adminapp/show_users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(ShowUsers, self).get_context_data(**kwargs)
        data['object_list'] = User.objects.all().order_by("-is_active", "username")
        return data

    def test_func(self):
        return self.request.user.is_superuser
=======
@user_passes_test(lambda u: u.is_superuser)
def show_users(request):
    users = User.objects.all().order_by("-is_active", "username")
    context = {
        "users": users,
    }
    return render(request, "adminapp/show_users.html", context)
>>>>>>> main
