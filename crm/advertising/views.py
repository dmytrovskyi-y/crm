from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from mixins import GroupRequiredMixin
from .forms import AdsForm
from .models import Ads


class AdsListView(LoginRequiredMixin, ListView):
    """Class view of advertising model."""
    queryset = Ads.objects.all()
    template_name = "ads/ads-list.html"
    context_object_name = "ads"


class AdsCreateView(GroupRequiredMixin, CreateView):
    """Class create new model Ads."""
    form_class = AdsForm
    template_name = "ads/ads-create.html"
    success_url = reverse_lazy("advertising:ads-list")
    group_required = ["Marketer"]


class AdsDetailView(DetailView):
    """Ads detail page display class."""
    template_name = "ads/ads-detail.html"

    def get_object(self, queryset=None):
        obj = get_object_or_404(Ads, id=self.kwargs["pk"])
        return obj
