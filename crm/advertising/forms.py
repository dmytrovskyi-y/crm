from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Ads


class AdsForm(ModelForm):
    """Class creating  form for model Ads."""

    class Meta:
        model = Ads
        fields = [
            "name",
            "promotion",
            "service",
            "budget"
        ]

    def clean_budget(self):
        """Check field budget, have to be >= 0."""
        budget = self.cleaned_data.get("budget", "")
        if budget < 0:
            raise ValidationError("Budget must be a positive number", code="invalid")
        return budget
