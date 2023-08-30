# Generated by Django 4.2 on 2023-05-17 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_address_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(choices=[('US', 'United States'), ('CA', 'Canada'), ('UK', 'United Kingdom'), ('INDIA', 'India')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona')], max_length=10, null=True),
        ),
    ]