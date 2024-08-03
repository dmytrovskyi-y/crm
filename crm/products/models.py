import uuid

from django.db import models


class Product(models.Model):
    """Model DB Service"""

    class Meta:
        ordering = ["name", "price"]
        verbose_name = "product"
        verbose_name_plural = "products"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, verbose_name="name")
    description = models.TextField(max_length=250, verbose_name="description")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("products:detail-product", kwargs={"id": self.id})

    def __str__(self) -> str:
        return f"{self.name} product."
