from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
import hashlib
from .models import User
import random


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ("username", "email", "avatar", "first_name", "last_name", "password")

    def save(self, *args, **kwargs):
        user = super().save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:6]
        user.activate_key = hashlib.sha1((user.email + salt).encode('utf-8')).hexdigest()
        user.save()
        return user


class UserEditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "avatar", "age")
