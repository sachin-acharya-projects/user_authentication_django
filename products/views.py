from django.http import HttpRequest
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.decorators import login_required


# Create your views here.
class HomeView(View):
    def get(self, request: HttpRequest):
        return render(request, "index.html")

    def post(self, request: HttpRequest):
        post = request.POST
        username = post.get("username")
        password = post.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "User has been authenticated successfully.")
            return redirect("products.dashboard")

        messages.error(request, "User is not authorized for the resource.")
        return redirect("products.home")


@login_required(login_url="products.home")
def home(request: HttpRequest):
    return render(request, "home.html")


@login_required(login_url="products.home")
def logout_user(request: HttpRequest):
    django_logout(request)
    messages.success(request, "You have been logged out")

    return redirect("products.home")
