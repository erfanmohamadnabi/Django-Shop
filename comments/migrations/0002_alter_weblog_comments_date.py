# Generated by Django 5.0.2 on 2024-10-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weblog_comments',
            name='date',
            field=models.CharField(default='1403/07/17', max_length=100, verbose_name='تاریخ'),
        ),
    ]