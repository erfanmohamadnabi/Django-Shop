# Generated by Django 5.0.2 on 2024-10-12 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_cart_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='code',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='کد سفارش'),
        ),
    ]
