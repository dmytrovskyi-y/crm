from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from mixins import GroupRequiredMixin
from .forms import ProductForm
from .models import Product


class ProductsListView(LoginRequiredMixin, ListView):
    """Product list View class"""
    queryset = Product.objects.filter(is_active=True)
    context_object_name = "products"
    template_name = "products/products-list.html"


class ProductCreateView(GroupRequiredMixin, CreateView):
    """Class create new model Product"""
    form_class = ProductForm
    template_name = "products/products-create.html"
    success_url = reverse_lazy("products:products-list")
    group_required = ["Marketer"]


class ProductDetailView(GroupRequiredMixin, DetailView):
    """Detail Product model View"""
    template_name = "products/products-detail.html"
    group_required = ["Marketer"]

    def get_object(self, queryset=None):
        return get_object_or_404(Product, id=self.kwargs["id"])


class ProductUpdateView(GroupRequiredMixin, UpdateView):
    """Class update a record in model Product"""
    form_class = ProductForm
    template_name = "products/products-edit.html"
    success_url = reverse_lazy("products:products-list")
    group_required = ["Marketer"]

    def get_object(self, queryset=None):
        return get_object_or_404(Product, id=self.kwargs["id"])


class ProductDeleteView(GroupRequiredMixin, DeleteView):
    """Class for deleting a record from a model Product"""
    model = Product
    template_name = "products/products-delete.html"
    success_url = reverse_lazy("products:products-list")
    group_required = ["Marketer"]

    def get_object(self, queryset=None):
        return get_object_or_404(Product, id=self.kwargs["id"])
