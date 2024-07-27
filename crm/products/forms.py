from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Product


class ProductForm(ModelForm):
    """Class for create  form for model Product"""

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price"
        ]

    def clean_price(self):
        print(self.cleaned_data)
        price = self.cleaned_data.get("price", "")
        if price < 0:
            raise ValidationError("Price must be a positive number", code="invalid")

        return price
