from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import IndexPageView, LoginUser

app_name = "users"

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
