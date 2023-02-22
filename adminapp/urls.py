from django.urls import path

from adminapp.views import (
    add_animal,
    add_type,
    add_user,
    delete_animal,
    delete_type,
    delete_user,
    detail_animal,
    edit_animal,
    edit_type,
    show_animal,
    show_users,
)

app_name = "adminapp"

urlpatterns = [
    path("add_type/create/", add_type, name="add_type"),
    path("delete_type/<int:pk>/", delete_type, name="delete_type"),
    path("edit_type/<int:pk>/", edit_type, name="edit_type"),
    path("add_animal/", add_animal, name="add_animal"),
    path("edit_animal/<int:pk>/", edit_animal, name="edit_animal"),
    path("delete_animal/<int:pk>/", delete_animal, name="delete_animal"),
    path("show_animals/<int:pk>/", show_animal, name="show_animal"),
    path("detail_animals/<int:pk>/", detail_animal, name="detail_animal"),
    path("add_user/", add_user, name="add_user"),
    path("delete_user/<int:pk>/", delete_user, name="delete_user"),
    path("show_users/", show_users, name="show_users"),
]