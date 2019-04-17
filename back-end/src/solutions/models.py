from django.db import models
from product.models import Product

class Solutions(models.Model):
    industry = models.CharField(max_length=100, default="default")
    description = models.TextField(default="default")
    implement_period = models.CharField(max_length=100, default="default")

    products = models.ManyToManyField(Product)

    def get_absolute_url(self):
        return reverse('solution-id', args=[str(self.id)])