from django.shortcuts import render
from .forms import SubscriberForm
from products.models import ProductImage


def landing(request):
    name = "themikhalych"
    # current_day = "19.03.2018"
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        # print(request.POST)
        # print(form.cleaned_data)
        data = form.cleaned_data
        # print(data["name"])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True,
                                                  product__is_active=True)
    products_images_phones = products_images.filter(product__category__name="Телефон")
    products_images_laptops = products_images.filter(product__category__name="Ноутбук")
    return render(request, 'landing/home.html', locals())


