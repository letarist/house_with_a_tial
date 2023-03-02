from django.urls import path

from adminapp.views import (
    add_animal,
    CreateType,
    DetailAnimal,
    add_user,
    DeleteAnimal,
    DeleteType,
    DeleteUser,
    add_user,
    edit_animal,
    edit_type,
    show_animal,
    show_users,
)

app_name = "adminapp"

urlpatterns = [
    path("add_type/create/", CreateType.as_view(), name="add_type"),
    path("delete_type/<int:pk>/", DeleteType.as_view(), name="delete_type"),
    path("edit_type/<int:pk>/", edit_type, name="edit_type"),
    path("add_animal/<int:pk>/", add_animal, name="add_animal"),
    path("edit_animal/<int:pk>/", edit_animal, name="edit_animal"),
    path("delete_animal/<int:pk>/", DeleteAnimal.as_view(), name="delete_animal"),
    path("show_animals/<int:pk>/", show_animal, name="show_animal"),
    path("detail_animals/<int:pk>/", DetailAnimal.as_view(), name="detail_animal"),
    path("add_user/", add_user, name="add_user"),
    path("delete_user/<int:pk>/", DeleteUser.as_view(), name="delete_user"),
    path("show_users/", show_users, name="show_users"),
]
