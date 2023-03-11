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


class ShowUsers(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'adminapp/show_users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super(ShowUsers, self).get_context_data(**kwargs)
        data['object_list'] = User.objects.all().order_by("-is_active", "username")
        return data

    def test_func(self):
        return self.request.user.is_superuser
