# Generated by Django 4.2 on 2023-05-13 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_color_variant_and_more'),
        ('accounts', '0003_alter_cartitems_options_alter_cartitems_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='color_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='color', to='products.colorvariant'),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_info', to='products.product'),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='size_variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='size', to='products.sizevariant'),
        ),
    ]
