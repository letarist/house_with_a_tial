from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.template.loader import render_to_string
from django.urls import reverse

from .models import Basket
from mainapp.models import Animal


@login_required
def basket_show(request):
    basket_list = Basket.objects.filter(user=request.user)
    title = 'Корзина'
    media_url = settings.MEDIA_URL
    context = {
        'basket_list': basket_list,
        'title': title,
        'media_url': media_url
    }
    return render(request, 'basketapp/basket.html', context)


@login_required
def basket_add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('mainapp:person_animal', args=[pk]))
    animal = get_object_or_404(Animal, pk=pk)
    basket = Basket.objects.filter(user=request.user, animal=animal).first()
    if not basket:
        basket = Basket(user=request.user, animal=animal)
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_delete(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def edit_basket(request, pk, quantity):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        new_basket_item = Basket.objects.get(pk=pk)
        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()
        basket_list = Basket.objects.filter(user=request.user)
        context = {
            'basket_list': basket_list,
            'media_url': settings.MEDIA_URL
        }
        result = render_to_string('basketapp/includes/inc_basket.html', context)
        return JsonResponse({'result': result})
