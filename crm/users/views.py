from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView

from products.models import Product


class IndexPageView(LoginRequiredMixin, TemplateView):
    """
    Class View hope(index) page.
    """
    template_name = "users/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products_count"] = Product.objects.count()
        return context


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "users/login.html"
