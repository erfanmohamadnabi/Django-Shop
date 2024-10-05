# Generated by Django 5.1 on 2024-10-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان پیام')),
                ('email', models.EmailField(max_length=1000, verbose_name='ایمیل کاربر')),
                ('message', models.TextField(verbose_name='متن پیام')),
            ],
            options={
                'verbose_name': 'اضافه کردن پیام',
                'verbose_name_plural': 'ارتباط با ما',
            },
        ),
    ]