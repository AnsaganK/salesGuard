from django.db import models
from pytils.translit import slugify
from django.shortcuts import reverse

from .base import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Subcategory(BaseModel):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, null=True, blank=True)

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='subcategories'
    )

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('app:subcategory_detail', args=[self.slug])
