# Step-By-Step Procedure

-   Create a Project

-   `{{ PROJECT_NAME }}/urls.py`

```diff
urlpatterns = [
    path("admin/", admin.site.urls),
+    path("product/", include("django.contrib.auth.urls")),
+    path("product/", include("products.urls")),
]
```

> ![NOTE]
> For both, endpoint 'product/' are same. First pattern handle authentication and second handle regular routing.


- Authenticating
[views.py](./products/views.py)