from django.http import JsonResponse
from .models import *
from django.shortcuts import render, redirect
from .forms import CheckoutContactForm
from django.contrib.auth.models import User


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    # print(request.POST)
    product_id = request.POST.get("product_id")
    nmb = request.POST.get("nmb")
    is_delete = request.POST.get("is_delete")

    if is_delete == 'true':
        ProductInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, is_created = ProductInBasket.objects.get_or_create(
                session_key=session_key,
                product_id=product_id,
                is_active=True,
                defaults={"nmb": nmb}
        )
        if not is_created:
            new_product.nmb += int(nmb)
            new_product.save(force_update=True)

    products_in_basket = ProductInBasket.objects.filter(
            session_key=session_key,
            is_active=True)
    products_total_nmb = products_in_basket.count()
    return_dict["products_total_nmb"] = products_total_nmb
    return_dict["products"] = list()

    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["nmb"] = item.nmb
        return_dict["products"].append(product_dict)

    return JsonResponse(return_dict)


def checkout(request):
    session_key = request.session.session_key
    # products_in_basket = ProductInBasket.objects.filter(
    #         session_key=session_key, is_active=True, order__isnull=True)
    # print(products_in_basket)
    # for item in products_in_basket:
    #     print(item.order)

    form = CheckoutContactForm(request.POST or None)
    if request.POST and form.is_valid():
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        user, created = User.objects.get_or_create(
                username=email,
                defaults={"first_name": name, "last_name": phone})
        order = Order.objects.create(
                user=user,
                customer_name=name,
                customer_phone=phone,
                customer_email=email,
                status_id=1)

        for name, value in request.POST.items():
            if name.startswith("product_in_basket_"):
                product_in_basket_id = name.split("product_in_basket_")[1]
                product_in_basket = ProductInBasket.objects.get(
                        id=product_in_basket_id)
                # print(type(value))

                product_in_basket.nmb = value
                product_in_basket.order = order
                product_in_basket.save(force_update=True)

                ProductInOrder.objects.create(
                        product=product_in_basket.product,
                        nmb=product_in_basket.nmb,
                        price_per_item=product_in_basket.price_per_item,
                        total_price=product_in_basket.total_price,
                        order=order)

        return redirect('order_saved/')
    return render(request, 'orders/checkout.html', locals())


def order_saved(request):
    return render(request, 'orders/order_saved.html')
