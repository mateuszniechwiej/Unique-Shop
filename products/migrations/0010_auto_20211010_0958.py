# Generated by Django 3.2.7 on 2021-10-10 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20211010_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='colour',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='colour',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]