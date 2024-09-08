from django.test import TestCase

from ..forms import ProductForm


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
        self.assertEqual(form.errors["price"][0], "Price must be a positive number")