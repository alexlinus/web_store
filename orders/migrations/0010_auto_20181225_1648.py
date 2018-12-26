# Generated by Django 2.1.4 on 2018-12-25 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20181225_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(blank=True, null=True, related_name='order_items', to='orders.Cart', verbose_name='Корзина этого заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Принят в обработку', 'Принят в обработку'), ('Оплачен', 'Оплачен'), ('Выполняется', 'Выполняется')], default='Принят в обработку', max_length=100),
        ),
    ]