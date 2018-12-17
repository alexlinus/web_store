# Generated by Django 2.1.4 on 2018-12-09 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(default='default.jpg', upload_to='uploads/product_images/')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
                ('is_main', models.BooleanField(default=False, verbose_name='Главное изображение')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='images',
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='store.Product'),
        ),
    ]