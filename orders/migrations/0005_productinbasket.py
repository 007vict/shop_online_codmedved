# Generated by Django 2.2.1 on 2019-06-06 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190523_1954'),
        ('orders', '0004_auto_20190523_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmb', models.IntegerField(default=1)),
                ('price_per_item', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('total_price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.Order')),
                ('product', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
            },
        ),
    ]
