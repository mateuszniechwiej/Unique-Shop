# Generated by Django 3.2.7 on 2021-10-10 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_variation_sizes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sizes',
            new_name='Size',
        ),
        migrations.CreateModel(
            name='Colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour', models.CharField(choices=[('red', 'RED'), ('yellow', 'YELLOW'), ('blue', 'BLUE')], default='red', max_length=120)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
