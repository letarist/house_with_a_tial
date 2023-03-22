from django.urls import path

from .views import change, login, logout, register, verify

app_name = "authapp"
urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("register", register, name="register"),
    path("change/", change, name="change"),
    path("verify/<email>/<activation_key>/", verify, name='verify')
]
