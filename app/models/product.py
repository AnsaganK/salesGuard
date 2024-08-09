import uuid

from django.db import models
from pytils.translit import slugify

from .base import BaseModel
from .category import Subcategory
from .client import Client


class Product(BaseModel):
    name = models.CharField(max_length=512, null=True, blank=True)
    slug = models.SlugField(max_length=512, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    img = models.ImageField(upload_to='products/', null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True, default=1)

    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='products'
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Order(BaseModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'

    def __str__(self):
        return f'Продажа №{self.id}'

    @property
    def get_sum(self):
        return self.product.price * self.quantity
