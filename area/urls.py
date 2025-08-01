
from django.urls import path

from area import views

app_name = "area"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact", views.contact, name="contact"),
    path("shop", views.shop, name="shop"),
    path("product/<uuid>", views.product, name="product"),
    path("shopping-cart", views.shopping_cart, name="shopping-cart"),
    path("checkout", views.checkout, name="checkout"),
    path("cart/add/<str:product_type>/<uuid:uuid>", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<str:product_type>/<uuid:uuid>", views.remove_from_cart, name="remove_from_cart"),
    path("search-results", views.search,name="search")
]
