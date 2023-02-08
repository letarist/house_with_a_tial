from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from .models import Basket
from mainapp.models import Animal


def basket_show(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_add(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    basket = Basket.objects.filter(user=request.user, animal=animal).first()
    if not basket:
        basket = Basket(user=request.user, animal=animal)
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_delete(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
