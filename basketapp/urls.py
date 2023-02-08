from django.urls import path
from .views import basket_show, basket_add, basket_delete

app_name = "basketapp"

urlpatterns = [
    path('', basket_show, name='basket_show'),
    path('add/<int:pk>/', basket_add, name='basket_add'),
    path('delete/<int:pk>/', basket_delete, name='basket_delete'),
]
