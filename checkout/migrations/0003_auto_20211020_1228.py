# Generated by Django 3.2.7 on 2021-10-20 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_order_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orginal_cart',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]
