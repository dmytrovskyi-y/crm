from django.contrib.auth.models import User, Group
from django.template.response import TemplateResponse
from django.test import TestCase, Client
from django.urls import reverse_lazy

from ..models import Ads


class ProductViewTestCase(TestCase):
    """Tests views Ad's app."""
    fixtures = [
        "fixtures/02-product-fixtures.json",
        "fixtures/05-ads-fixtures.json",
    ]

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()

        cls.data = {
            "user": User.objects.create(username="Tester", password="password123"),
            "ads": Ads.objects.all(),
            "ads_url": reverse_lazy("advertising:ads-list"),
            "ads_template": "ads/ads-list.html",
            "create_url": reverse_lazy("advertising:create-ads"),
            "create_data": {
                "name": "Test Product",
                "description": "This is test description",
                "price": 700
            },
        }
        Group.objects.create(name="Marketer")
        group = Group.objects.get(name="Marketer")
        cls.data["user"].groups.add(group)
        cls.data["user"].save()

    def setUp(self):
        self.client = Client()
        self.client.force_login(self.data["user"])

    @classmethod
    def tearDownClass(cls):
        cls.data["user"].delete()

    def test_product_list_view(self):
        """
        Testing class AdsListView response status code, template, display of data on page.
        :return: None
        """
        response: TemplateResponse = self.client.get(self.data["ads_url"])

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, self.data["ads_template"])
        self.assertEqual(list(self.data["ads"]), list(response.context_data["ads"]))
