from django.db import models

from .base import BaseModel


class Client(BaseModel):
    name = models.CharField(max_length=128, null=True, blank=True)

    last_name = models.CharField(max_length=128, null=True, blank=True)
    first_name = models.CharField(max_length=128, null=True, blank=True)
    patronymic = models.CharField(max_length=128, null=True, blank=True)

    email = models.EmailField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.get_full_name

    @property
    def get_full_name(self):
        full_name = ''
        full_name += f'{self.last_name}' if self.last_name else ''
        full_name += f' {self.first_name}' if self.first_name else ''
        full_name += f' {self.patronymic}' if self.patronymic else ''
        return full_name.strip()

    @property
    def get_name(self):
        if self.name:
            return self.name
        return self.get_full_name
