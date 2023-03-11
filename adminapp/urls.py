from django.urls import path

from adminapp.views import (

    AddAnimal,
    CreateType,
    DetailAnimal,
    AddUser,
    DeleteAnimal,
    DeleteType,
    DeleteUser,
    EditAnimal,
    EditType,
    ShowAnimal,
    ShowUsers
)

app_name = "adminapp"

urlpatterns = [
    path("add_type/create/", CreateType.as_view(), name="add_type"),
    path("delete_type/<int:pk>/", DeleteType.as_view(), name="delete_type"),
    path("edit_type/<int:pk>/", EditType.as_view(), name="edit_type"),
    path("add_animal/<int:pk>/", AddAnimal.as_view(), name="add_animal"),
    path("edit_animal/<int:pk>/", EditAnimal.as_view(), name="edit_animal"),
    path("delete_animal/<int:pk>/", DeleteAnimal.as_view(), name="delete_animal"),
    path("show_animals/<int:pk>/", ShowAnimal.as_view(), name="show_animal"),
    path("detail_animals/<int:pk>/", DetailAnimal.as_view(), name="detail_animal"),
    path("add_user/", AddUser.as_view(), name="add_user"),
    path("delete_user/<int:pk>/", DeleteUser.as_view(), name="delete_user"),
    path("show_users/", ShowUsers.as_view(), name="show_users"),
]
