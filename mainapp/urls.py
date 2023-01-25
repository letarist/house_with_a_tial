from django.urls import path

from .views import index, contact, animal_of_types

app_name = 'mainapp'
urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('<int:pk>', animal_of_types, name='animaloftype')
]
