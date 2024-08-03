from django.urls import path

from .views import (
    ProductsListView,
    ProductCreateView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = "products"

urlpatterns = [
    path("", ProductsListView.as_view(), name="products-list"),
    path("create/", ProductCreateView.as_view(), name="create-product"),
    path("detail/<uuid:id>", ProductDetailView.as_view(), name="detail-product"),
    path("update/<uuid:id>", ProductUpdateView.as_view(), name="update-product"),
    path("delete/<uuid:id>", ProductDeleteView.as_view(), name="delete-product"),
]
