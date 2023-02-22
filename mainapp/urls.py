from django.urls import path

from .views import animal_of_types, contact, person_animal

app_name = "mainapp"
urlpatterns = [
    path("", animal_of_types, name="typeanimal"),
    path("contact/", contact, name="contact"),
    path("<int:pk>/", animal_of_types, name="animaloftype"),
    path("animal/<int:pk>/", person_animal, name="person_animal"),
]
