from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from products.models import Product


class IndexPageView(LoginRequiredMixin, TemplateView):
    """
    Class View hope(index) page.
    """
    template_name = "users/index.html"
    login_url = "/admin/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products_count"] = Product.objects.count()
        return context
