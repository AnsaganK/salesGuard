# Generated by Django 5.0.6 on 2024-08-09 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_sale_delete_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sale',
            new_name='Order',
        ),
    ]
