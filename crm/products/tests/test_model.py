from django.test import TestCase
from ..models import Product


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