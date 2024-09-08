from django.db import models

from products.models import Product


class Ads(models.Model):
    """Model (DB) of an advertising company"""
    class Meta:
        ordering = ["date"]
        verbose_name = "ad"
        verbose_name_plural = "ads"

    name = models.CharField(max_length=250, verbose_name="name")
    service = models.ManyToManyField(Product, related_name="service", name="service")
    promotion = models.CharField(max_length=500, verbose_name="promotion channel")
    budget = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="budget")
    date = models.DateField(auto_now_add=True, verbose_name="creation date")

    def __str__(self):
        return self.name
