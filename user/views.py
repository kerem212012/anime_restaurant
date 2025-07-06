from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from user.forms import UserLoginForm, UserRegisterForm


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
    return render(request, "user/login.html", context={"form": form})


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
    return render(request, "user/registration.html", context={"form": form})


def user_logout(request):
    logout(request)
    return redirect("/")
