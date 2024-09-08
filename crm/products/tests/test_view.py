from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.test import TestCase, Client
from django.urls import reverse_lazy, reverse

from ..models import Product


class ProductViewTestCase(TestCase):
    """
    Tests views Product's app
    """
    fixtures = [
        "fixtures/02-product-fixtures.json",
        # "fixtures/04-grope-fixtures.json",
    ]

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.data = {
            "user": User.objects.create(username="Tester", password="password123"),
            "product": Product.objects.filter(is_active=True),
            "list_url": reverse_lazy("products:products-list"),
            "list_template": "products/products-list.html",
            "create_url": reverse_lazy("products:create-product"),
            "create_data": {
                "name": "Test Product",
                "description": "This is test description",
                "price": 700
            },
            "detail_url": reverse(
                "products:detail-product",
                kwargs={"id": Product.objects.filter(is_active=True).first().id}
            ),
            "detail_template": "products/products-detail.html",
            "new_product": Product.objects.create(
                name="Test name", description="This is test description", price=200, is_active=True
            ),
            "update_data": {
                "name": "Test Product",
                "description": "This is test description",
                "price": 800
            }
        }
        # print(Group.objects.all())
        Group.objects.create(name="Marketer")
        group = Group.objects.get(name="Marketer")
        cls.data["user"].groups.add(group)
        cls.data["user"].save()

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.data["user"])

    @classmethod
    def tearDownClass(cls):
        cls.data["new_product"].delete()

    def test_product_list_view(self):
        """
        Testing class ProductListView response status code, template, display of data on page.
        :return: None
        """
        response: TemplateResponse = self.client.get(self.data["list_url"])

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.data["list_template"])
        self.assertEqual(list(self.data["product"]), list(response.context_data["products"]))

    def test_product_detail_view(self):
        """
        Testing ProductDetailView class. Check response's status code, template and object.
        Giving 'pk' of product from Products table as a key of url id.
        :return: None
        """

        response: TemplateResponse = self.client.get(self.data["detail_url"])
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.data["detail_template"])
        self.assertEqual(self.data["product"].first(), response.context_data["object"])

    def test_product_create_view(self):
        """
        Testing ProductCreateView response status code, template, correct created test product.
        Sending post request to ProductCreateView with new product data.
        :return: None
        """

        response: HttpResponseRedirect = self.client.post(
            self.data["create_url"], data=self.data["create_data"]
        )
        self.assertRedirects(response, reverse_lazy("products:products-list"), status_code=302)
        self.assertTrue(Product.objects.filter(name=self.data["create_data"]["name"]).exists())

    def test_product_update_view(self):
        """
        Testing ProductUpdateView class.
        Create new product and change its price.
        Sending post request to ProductUpdateView with new product price.
        :return: None
        """
        obj = self.data["new_product"]
        response = self.client.post(
            reverse("products:update-product", kwargs={"id": obj.id}), data=self.data["update_data"]
        )
        obj.refresh_from_db()
        self.assertRedirects(response, reverse_lazy("products:products-list"), status_code=302)
        self.assertEqual(obj.price, 800.00)

    def test_product_delete_view(self):
        """
        Testing ProductDeleteView class.
        Sending request with id Product model as the key for delete this Product from DB.
        :return: None
        """
        obj_id = self.data["new_product"].id
        response = self.client.post(reverse("products:delete-product", kwargs={"id": obj_id}))
        self.assertRedirects(response, reverse_lazy("products:products-list"), status_code=302)
        self.assertFalse(Product.objects.filter(id=obj_id).exists())
