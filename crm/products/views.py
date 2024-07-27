from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import ProductForm
from .models import Product


class ProductsListView(ListView):
    """Product List View Class"""
    queryset = Product.objects.all()
    context_object_name = "products"


class ProductCreateView(CreateView):
    """Class create new model Product"""
    form_class = ProductForm
    template_name = "products/products-create.html"
    success_url = reverse_lazy("products:products-list")
