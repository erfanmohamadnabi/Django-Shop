# Generated by Django 5.0.2 on 2024-10-08 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='buy',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20, verbose_name='تعداد فروش'),
        ),
        migrations.AddField(
            model_name='product',
            name='keywords',
            field=models.CharField(default=1, max_length=500, verbose_name='کلیدواژه ها را برای سئو وارد کنید (  با علامت , جدا کنید  )'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='meta_seo',
            field=models.TextField(default=1, verbose_name='توضیحات متا برای سئو'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='ranking_AVG',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=20, null=True, verbose_name='رنکینگ محصول'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_seo',
            field=models.CharField(default=1, max_length=500, verbose_name='عنوان برای سئو'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='visit',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20, verbose_name='تعداد بازدید'),
        ),
        migrations.CreateModel(
            name='Product_Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_image', verbose_name='تصویر محصول')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'تصویر جدید',
                'verbose_name_plural': 'اضافه کردن تصویر محصول',
            },
        ),
    ]
