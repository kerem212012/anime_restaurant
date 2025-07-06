from django.contrib.auth import login, logout, authenticate
from django.http import Http404
from django.shortcuts import render, redirect

from area.models import Food, FoodCategory, MerchCategory, Merch, Event
from user.forms import UserRegisterForm, UserLoginForm


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
        "events":event,
    }
    return render(request, "index.html", context=context)


def contact(request):
    return render(request, "contact.html")


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
    return render(request, "shop.html", context=context)


def product(request, uuid):
    product = (Food.objects.filter(uuid=uuid).first() or Merch.objects.filter(uuid=uuid).first())
    if not product:
        raise Http404("Продукт не найден")

    return render(request, 'shop-details.html', {
        'product': product,
        'product_type': product._meta.model_name
    })




def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")

    else:
        form = UserLoginForm()
    return render(request, "login.html", context={"form": form})


def registration_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get("password")
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect("/")
    else:
        form = UserRegisterForm()
    return render(request, "registration.html", context={"form": form})


def user_logout(request):
    logout(request)
    return redirect("/")
