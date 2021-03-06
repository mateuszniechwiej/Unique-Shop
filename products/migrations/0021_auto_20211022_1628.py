# Generated by Django 3.2.7 on 2021-10-22 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0020_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='sku',
        ),
        migrations.AddField(
            model_name='review',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='products.product'),
        ),
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='profiles.userprofile'),
        ),
    ]
