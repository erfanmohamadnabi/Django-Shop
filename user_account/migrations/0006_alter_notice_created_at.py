# Generated by Django 5.0.2 on 2024-10-16 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0005_alter_user_address_options_alter_notice_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='created_at',
            field=models.CharField(default='1403/07/25', max_length=1000, verbose_name='تاریخ ایجاد'),
        ),
    ]
