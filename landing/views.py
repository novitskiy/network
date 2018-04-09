from django.shortcuts import render
from .forms import SubscriberForm
from products.models import ProductImage
from .models import Subscriber


def home(request):
    products_images = ProductImage.objects.filter(
            is_active=True, is_main=True, product__is_active=True
    )
    products_images_phones = products_images.filter(
            product__category__name="Телефон"
    )
    products_images_laptops = products_images.filter(
            product__category__name="Ноутбук"
    )
    return render(request, 'landing/home.html', locals())


def email_saved(request):
    if request.method == "POST":
        subscriber_form = SubscriberForm(request.POST)
        if subscriber_form.is_valid():
            subscriber_email = request.POST.get('email')
            new_subscriber, is_created = Subscriber.objects.get_or_create(
                email=subscriber_email
            )
            subscriber_form = SubscriberForm()
    return render(request, 'landing/email_saved.html', locals())


# def landing(request):
#     form = SubscriberForm(request.POST or None)
#
#     if request.method == "POST" and form.is_valid():
#         # print(request.POST)
#         # print(form.cleaned_data)
#         data = form.cleaned_data
#         # print(data["name"])
#
#         new_form = form.save()
#
#     return render(request, 'landing/landing.html', locals())
