from django.template.response import TemplateResponse
from django.test import TestCase, Client
from django.urls import reverse_lazy

from .forms import ProductForm
from .models import Product


class ProductModelTestCase(TestCase):
    """
    App Model Tests Products
    """
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.product = Product.objects.create(name="test_name", description="test_description", price=10.50)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.product.delete()

    def test_correct_creating_new_product(self):
        """
        Test of correct creation of a model object Product.
        :return: None
        """
        expected_data = ["test_name", "test_description", 10.50]
        new_obj_data = [self.product.name, self.product.description, self.product.price]
        self.assertSequenceEqual(expected_data, new_obj_data)


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
        :return: None
        """
        response: TemplateResponse = self.client.get(self.product_list_view_data["url"])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.product_list_view_data["template"])

    def test_product_list_view_correct_data(self):
        """
        Test of correct display of data on page.
        :return: None
        """
        response: TemplateResponse = self.client.get(self.product_list_view_data["url"])
        self.assertEqual(list(self.product_list_view_data["products"]), list(response.context_data["products"]))


class FormTestCase(TestCase):
    """
    Tests ProductForm form.
    """
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.correct_data_form = {
            "name": "test_name",
            "description": "test_description",
            "price": 20.88
        }

    def test_form_with_correct_data(self):
        """
        Test form with correct data and waited passing of form.is_valid().
        :return: None
        """
        form = ProductForm(data=self.correct_data_form)
        self.assertTrue(form.is_valid())

    def test_price_with_incorrect_data(self):
        """
        Testing a form with incorrect data (price < 0) sent to it.
        :return: None
        """
        self.correct_data_form["price"] = -1.99
        form = ProductForm(data=self.correct_data_form)
        self.assertFalse(form.is_valid())
