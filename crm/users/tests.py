from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse_lazy

from products.models import Product


class UsersTestCase(TestCase):
    """
    Tests Users app
    """
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="mimia", password="momo123123")
        cls.index_page = reverse_lazy("users:index")
        cls.index_view_context_data = {
            "products_count": Product.objects.count()
        }

    def setUp(self):
        self.client.force_login(self.user)

    def test_index_page_without_authentication(self):
        """Test index page without authentication."""
        logout(self.client)
        response: HttpResponseRedirect = self.client.get(self.index_page)
        self.assertEqual(response.status_code, 302)

    def test_index_page_with_authentication(self):
        """Test index page with authentication."""
        response: TemplateResponse = self.client.get(self.index_page)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name[0], "users/index.html")

    def test_correct_count_data(self):
        """Test displaying correct data on pages"""
        response: TemplateResponse = self.client.get(self.index_page)
        self.assertEqual(response.context_data["products_count"], self.index_view_context_data["products_count"])
