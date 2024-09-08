from django.test import TestCase

from products.models import Product
from ..models import Ads


class AdsModelTestCase(TestCase):
    """Testing correct Ads model creation."""
    fixtures = [
        "fixtures/02-product-fixtures.json",
    ]

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.product = Product.objects.first()
        cls.ads = Ads(
            name="test_name",
            promotion="test_promotion",
            budget=250,
        )
        cls.ads.save()
        cls.ads.service.add(cls.product)

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.product.delete()

    def test_correct_creating_new_ads(self):
        """
        Test of correct creation of a model object Ads.
        :return: None
        """

        expected_data = ["test_name", [self.product,], "test_promotion", 250.00]
        new_ads_data = [self.ads.name, list(self.ads.service.all()), self.ads.promotion, self.ads.budget]
        self.assertSequenceEqual(expected_data, new_ads_data)
