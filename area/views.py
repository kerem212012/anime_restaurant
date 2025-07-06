from django.http import Http404
from django.shortcuts import render

from area.models import Food, FoodCategory, MerchCategory, Merch, Event
from manager.forms import ManagerFeedbackForm
from manager.models import Feedback


def index(request):
    foods = Food.objects.all()
    food_categories = FoodCategory.objects.all()
    merch_categories = MerchCategory.objects.all()
    merchs = Merch.objects.all()
    event = Event.objects.all()
    context = {
        "foods": foods,
        "food_categories": food_categories,
        "merch_categories": merch_categories,
        "merchs": merchs,
        "events": event,
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
