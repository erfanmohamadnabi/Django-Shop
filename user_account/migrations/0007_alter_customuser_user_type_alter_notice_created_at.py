# Generated by Django 5.0.2 on 2024-10-16 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0006_alter_notice_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('user', 'user'), ('sender', 'sender'), ('cashier', 'cashier'), ('middle_manager', 'middle_manager')], default='user', max_length=1000, verbose_name='نوع کاربر'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='created_at',
            field=models.CharField(default='1403/07/26', max_length=1000, verbose_name='تاریخ ایجاد'),
        ),
    ]
