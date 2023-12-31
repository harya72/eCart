# Generated by Django 4.2 on 2023-05-13 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_color_variant_and_more'),
        ('accounts', '0004_alter_cartitems_color_variant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='p', to='products.product'),
        ),
    ]
