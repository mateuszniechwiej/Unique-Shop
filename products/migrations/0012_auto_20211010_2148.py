# Generated by Django 3.2.7 on 2021-10-10 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_product_has_more_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_currency',
        ),
        migrations.RemoveField(
            model_name='size',
            name='price_currency',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='size',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]