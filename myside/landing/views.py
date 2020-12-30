from django.shortcuts import render
from .forms import SubscriberForm
from products.models import ProductImage


def landing(request):
    form = SubscriberForm(request.POST or None)  # Принемается реквест пост или нечего
    # форма на странице и сохроняем ее в админке
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data["name"])
        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    # Все продукты
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    # тодлько Чизкейки
    products_images_jizkeyc = products_images.filter(product__category__id=4)
    # только заварное
    products_images_zavar = products_images.filter(product__category__id=3)
    # только выпечка
    products_images_vipechka = products_images.filter(product__category__id=2)
    return render(request, 'landing/home.html', locals())
