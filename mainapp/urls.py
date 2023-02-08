from django.urls import path

from .views import animal_of_types, contact, index

app_name = "mainapp"
urlpatterns = [
    path("", animal_of_types, name="typeanimal"),
    path("contact/", contact, name="contact"),
    path("<int:pk>/", animal_of_types, name="animaloftype"),
]
