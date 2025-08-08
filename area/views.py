from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from area.forms import CheckoutForm
from area.models import Event, Order, OrderElement, Product, ProductCategory
from manager.forms import ManagerFeedbackForm
from manager.models import Feedback


def index(request):
    products = Product.objects.all()
    product_categories = ProductCategory.objects.all()
    events = Event.objects.select_related("anime").all()
    context = {
        "products": products,
        "product_categories": product_categories,
        "events": events,
    }
    return render(request, "area/index.html", context=context)


def search(request):
    query = request.GET.get("q", "").strip()
    products = []
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query)
        )
    return render(request, "area/search-results.html", context={
        "query": query,
        "products": products,
        "results_count": len(products)
    })


def contact(request):
    if request.method == "POST":
        form = ManagerFeedbackForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            message = form.cleaned_data.get("message")
            Feedback.objects.create(name=name, email=email, message=message)
    else:
        form = ManagerFeedbackForm()
    return render(request, "area/contact.html", context={"form": form})


def shop(request):
    min_price = request.GET.get("min_price")
    max_price = request.GET.get("max_price")

    products = Product.objects.all()
    product_categories = ProductCategory.objects.all()
    products_count = Product.objects.count()

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    context = {
        "products": products,
        "product_categories": product_categories,
        "products_count": products_count,
    }
    return render(request, "area/shop.html", context=context)


def product(request, uuid):
    product = Product.objects.filter(uuid=uuid).first()
    if not product:
        raise Http404("Продукт не найден")

    return render(request, 'area/shop-details.html', {
        'product': product,
        'product_type': product._meta.model_name
    })


@login_required
def shopping_cart(request):
    order = Order.objects.filter(user=request.user, is_draft=True).first()
    items = order.orders.all() if order else []
    total = sum(item.price * item.quantity for item in items)
    return render(request, "area/shopping-cart.html", context={
        "order": order,
        "items": items,
        "total": total,
    })


@login_required
def checkout(request):
    order = Order.objects.filter(user=request.user, is_draft=True).first()
    items = order.orders.all() if order else []
    total = sum(item.price * item.quantity for item in items)
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data.get("address")
            order_note = form.cleaned_data.get("order_note")
            Order.objects.update(user=request.user, address=address, is_draft=False, order_note=order_note, status="M")
            return redirect("/")
    else:
        form = CheckoutForm()
    return render(request, "area/checkout.html", context={"form": form, "items": items,
                                                          "total": total, })


@login_required
def add_to_cart(request,  uuid):
    product = get_object_or_404(Product, uuid=uuid)
    order, _ = Order.objects.get_or_create(user=request.user, is_draft=True)
    element = OrderElement.objects.filter(order=order,product=product).first()
    if element:
        element.quantity += 1
        element.save()
    else:
        OrderElement.objects.create(order=order, quantity=1, product=product,
                                    price=product.price)
    return redirect("area:shopping-cart")


@login_required
def remove_from_cart(request, uuid):
    product = get_object_or_404(Product,uuid=uuid)
    order, _ = Order.objects.get_or_create(user=request.user, is_draft=True)
    if not order:
        return redirect("area:shopping-cart")
    element = OrderElement.objects.filter(order=order, product=product).first()
    if element:
        element.delete()
    return redirect("area:shopping-cart")
