
from django.urls import path

from area import views

app_name = "area"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("shop", views.shop, name="shop"),
    path("product/<uuid>", views.product, name="product"),
]
