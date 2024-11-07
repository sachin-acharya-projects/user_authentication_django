from django.urls import path
from products.views import HomeView, home, logout_user

urlpatterns = [
    path("", HomeView.as_view(), name="products.home"),
    path("dashboard/", home, name="products.dashboard"),
    path("quit/", logout_user, name="products.logout")
]
