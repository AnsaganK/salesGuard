from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models import BaseModel


class Profile(BaseModel):
    class RoleChoices(models.TextChoices):
        ADMIN = 'admin', 'Администратор'
        MANAGER = 'manager', 'Менеджер'

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    patronymic = models.CharField(max_length=256, null=True, blank=True, verbose_name='Отчество')
    password = models.CharField(max_length=256, null=True, blank=True, verbose_name='Пароль')
    role = models.CharField(max_length=256, default=RoleChoices.MANAGER, choices=RoleChoices.choices)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'Профиль ({self.get_role_display()}) "{self.user.username}"'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
