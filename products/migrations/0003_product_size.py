# Generated by Django 3.2.7 on 2021-10-05 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211005_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
