from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class IndexPageView(LoginRequiredMixin, TemplateView):
    """
    Class View hope(index) page.
    """
    template_name = "users/index.html"
    login_url = "/admin/"
    def get_context_data(self, **kwargs):
        ...
