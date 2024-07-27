from django.template.response import TemplateResponse
from django.test import TestCase, Client
from django.urls import reverse_lazy

from products.models import Product



class ProductModelTestCase(TestCase):
    """
    App Model Tests Products
    """
    @classmethod
    def setUpTestData(cls):
        ...


class ProductViewTestCase(TestCase):
    """
    Tests views Product's app
    """
    fixtures = [
        "fixtures/02-product-fixtures.json",
    ]

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.product_list_view_data = {
            "products": Product.objects.all(),
            "url": reverse_lazy("products:products-list"),
            "template": "products/product_list.html",
        }

    def setUp(self):
        self.client = Client()

    def test_product_list_view(self):
        """
        Test class ProductListView response status code, template.
        """
        response: TemplateResponse = self.client.get(self.product_list_view_data["url"])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.product_list_view_data["template"])

    def test_product_list_view_correct_data(self):
        """Test of correct display of data on page."""
        response: TemplateResponse = self.client.get(self.product_list_view_data["url"])
        self.assertEqual(list(self.product_list_view_data["products"]), list(response.context_data["products"]))


class FormTestCase(TestCase):
    ...
