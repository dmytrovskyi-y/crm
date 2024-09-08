from django.test import TestCase

from products.models import Product
from ..forms import AdsForm


class FormTestCase(TestCase):
    """Tests AdsForm form."""
    fixtures = [
        "fixtures/02-product-fixtures.json",
    ]

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.product = Product.objects.first()
        cls.data_form = {
            "name": "test_name",
            "promotion": "test_promotion",
            "service": [cls.product,],
            "budget": 20.88
        }

    def test_form_with_correct_data(self):
        """
        Test form with correct data.
        Wait passing of form.is_valid().
        :return: None
        """

        form = AdsForm(data=self.data_form)
        self.assertTrue(form.is_valid())

    def test_price_with_incorrect_data(self):
        """
        Testing a form with incorrect data (budget < 0) sent to it.
        :return: None
        """

        self.data_form["budget"] = -1.99
        form = AdsForm(data=self.data_form)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["budget"][0], "Budget must be a positive number")
