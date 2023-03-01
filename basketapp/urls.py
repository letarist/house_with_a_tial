from django.urls import path

from .views import basket_add, basket_delete, basket_show, edit_basket

app_name = "basketapp"

urlpatterns = [
    path("", basket_show, name="basket_show"),
    path("add/<int:pk>/", basket_add, name="basket_add"),
    path("delete/<int:pk>/", basket_delete, name="basket_delete"),
    path("edit/<int:pk>/<int:quantity>/", edit_basket, name="edit_basket"),
]
