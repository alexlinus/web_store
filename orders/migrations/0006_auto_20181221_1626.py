# Generated by Django 2.1.4 on 2018-12-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20181221_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=10, null=True, verbose_name='Цена'),
        ),
    ]