from django.views.generic import ListView

from .models import Product


class ProductsListView(ListView):
    """Product List View Class"""
    model = Product
