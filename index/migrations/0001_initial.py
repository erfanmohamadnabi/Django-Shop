# Generated by Django 5.0.2 on 2024-10-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index_Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titie', models.CharField(max_length=1000, verbose_name='عنوان تصویر')),
                ('image', models.ImageField(upload_to='slider', verbose_name='تصویر')),
                ('link', models.TextField(verbose_name='لینک')),
            ],
            options={
                'verbose_name': 'اضافه کردن اسلایدر',
                'verbose_name_plural': 'اسلایدر صفحه اصلی',
            },
        ),
    ]