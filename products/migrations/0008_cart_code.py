# Generated by Django 5.0.2 on 2024-10-11 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_cart_created_at_cart_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='code',
            field=models.CharField(default=1, max_length=1000, verbose_name='کد سفارش'),
            preserve_default=False,
        ),
    ]
