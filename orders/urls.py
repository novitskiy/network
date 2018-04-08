from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^basket_adding/$', views.basket_adding, name='basket_adding'),
    re_path(r'^checkout/$', views.checkout, name='checkout'),
    re_path(r'^checkout/order_saved/$', views.order_saved, name='order_saved')
]
