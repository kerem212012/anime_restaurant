from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from area.models import Food, FoodCategory, MerchCategory, Merch, Event, Order, OrderElement
from manager.forms import ManagerFeedbackForm
from manager.models import Feedback


def index(request):
    foods = Food.objects.all()
    food_categories = FoodCategory.objects.all()
    merch_categories = MerchCategory.objects.all()
    merchs = Merch.objects.all()
    events = Event.objects.select_related("anime").all()
    context = {
        "foods": foods,
        "food_categories": food_categories,
        "merch_categories": merch_categories,
        "merchs": merchs,
        "events": events,
    }
    return render(request, "area/index.html", context=context)


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
    foods = Food.objects.all()
    food_categories = FoodCategory.objects.all()
    merch = Merch.objects.all()
    products_count = Food.objects.count() + Merch.objects.count()
    merchs = Merch.objects.all()
    context = {
        "foods": foods,
        "food_categories": food_categories,
        "merch": merch,
        "products_count": products_count,
        "merchs": merchs
    }
    return render(request, "area/shop.html", context=context)


def product(request, uuid):
    product = (Food.objects.filter(uuid=uuid).first() or Merch.objects.filter(uuid=uuid).first())
    if not product:
        raise Http404("Продукт не найден")

    return render(request, 'area/shop-details.html', {
        'product': product,
        'product_type': product._meta.model_name
    })

def shopping_cart(request):
    order = Order.objects.filter(user=request.user,is_draft=True).first()
    items = order.orders.all() if order else []
    total = sum(item.price * item.quantity for item in items)
    return render(request,"area/shopping-cart.html",context={
        "order":order,
        "items":items,
        "total":total,
    })

def checkout(request):
    return render(request,"area/checkout.html")

@login_required
def add_to_cart(request, product_type,uuid):
    content_type = get_object_or_404(ContentType,model=product_type)
    model_class = content_type.model_class()
    product=get_object_or_404(model_class,uuid=uuid)
    order,_=Order.objects.get_or_create(user=request.user,is_draft=True)
    element = OrderElement.objects.filter(order=order,content_type=content_type,object_id=product.id).first()
    if element:
        element.quantity += 1
        element.save()
    else:
        OrderElement.objects.create(order=order,content_type=content_type,object_id=product.id,quantity=1,price=product.price)
    return redirect("area:shopping-cart")

@login_required
def remove_from_cart(request, product_type,uuid):
    content_type = get_object_or_404(ContentType, model=product_type)
    model_class = content_type.model_class()
    product = get_object_or_404(model_class, uuid=uuid)
    order, _ = Order.objects.get_or_create(user=request.user, is_draft=True)
    if not order:
        return redirect("area:shopping-cart")
    element = OrderElement.objects.filter(order=order, content_type=content_type, object_id=product.id).first()
    if element:
        element.delete()
    return redirect("area:shopping-cart")
