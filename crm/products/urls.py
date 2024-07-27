from django.urls import path

from .views import ProductsListView, ProductCreateView

app_name = "products"

urlpatterns = [
    path("", ProductsListView.as_view(), name="products-list"),
    path("create/", ProductCreateView.as_view(), name="create-product"),
]
