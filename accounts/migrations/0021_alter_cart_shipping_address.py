# Generated by Django 4.2 on 2023-05-20 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_remove_address_cart_cart_shipping_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='shipping_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cart', to='accounts.address'),
        ),
    ]
