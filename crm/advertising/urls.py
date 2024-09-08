from django.urls import path
from .views import AdsListView, AdsCreateView, AdsDetailView

app_name = "advertising"

urlpatterns = [
    path("", AdsListView.as_view(), name="ads-list"),
    path("create/", AdsCreateView.as_view(), name="create-ads"),
    path("detail/<int:pk>", AdsDetailView.as_view(), name="detail-ads"),
]
