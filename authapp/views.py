from django.conf import settings
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, redirect, render, reverse

from .forms import LoginForm, UserEditForm, UserRegisterForm


def login(request):
    login_form = LoginForm(data=request.POST or None)
    next_param = request.GET.get("next", "")
    if request.method == "POST" and login_form.is_valid():
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)
        if user.is_active and user:
            auth.login(request, user)
            if "next_param" in request.POST.keys():
                return HttpResponseRedirect(request.POST.get("next_param"))
            return HttpResponseRedirect(reverse("index"))
    context = {"login_form": login_form, "next_param": next_param}
    return render(request, "authapp/login.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        register_form = UserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        register_form = UserRegisterForm()
    context = {"register_form": register_form, "media_url": settings.MEDIA_URL}
    return render(request, "authapp/register.html", context)


def change(request):
    if request.method == "POST":
        edit_user_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_user_form.is_valid():
            edit_user_form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        edit_user_form = UserEditForm(instance=request.user)
    context = {"edit_user_form": edit_user_form, "media_url": settings.MEDIA_URL}
    return render(request, "authapp/change_user.html", context)
