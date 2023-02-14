from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
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
