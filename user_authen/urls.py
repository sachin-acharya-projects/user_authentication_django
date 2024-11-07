from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("product/", include("django.contrib.auth.urls")),
    path("product/", include("products.urls")),
]


admin.site.site_header = "User Authen Dashboard"
admin.site.site_title = "Dashboard"
admin.site.index_title = "Welcome to Dashboard"
