from django.urls import path

from .views import ProductsListView

app_name = "products"

urlpatterns = [
    path("list/", ProductsListView.as_view(), name="products-list"),
]
