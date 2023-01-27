from django.urls import path
from .views import login, logout, register, change

app_name = 'authapp'
urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register', register, name='register'),
    path('change/', change, name='change')
]
