from django.conf import settings
from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, redirect, render, reverse
from django.core.mail import send_mail

from .forms import LoginForm, UserEditForm, UserRegisterForm
from .models import User


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
            user = register_form.save()
            if create_mail(user):
                return HttpResponseRedirect(reverse('authapp:login'))
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


def verify(requset, email, activation_key):
    user = User.objects.get(email=email)
    if user.activate_key == activation_key and user.is_user_activation_key_expired():
        user.is_active = True
        user.save()
        auth.login(requset, user)
        return render(requset, 'authapp/verification.html')
    else:
        return render(requset, 'authapp/verification.html')


def create_mail(user):
    verify_link = reverse('authapp:verify', args=[user.email, user.activate_key])
    title = f'Подтверждение учетной записи'
    body_message = f'Привет, {user.username}! Ваша ссылка для активации аккаунта {settings.HOST}{verify_link}'
    return send_mail(title, body_message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
