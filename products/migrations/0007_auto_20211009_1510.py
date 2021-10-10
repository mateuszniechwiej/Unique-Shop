# Generated by Django 3.2.7 on 2021-10-09 14:10

from django.db import migrations, models
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='name',
        ),
        migrations.AddField(
            model_name='variation',
            name='size',
            field=models.CharField(choices=[('small', 'S'), ('medium', 'M'), ('large', 'L')], default='small', max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default_currency='EUR', max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='price',
            field=djmoney.models.fields.MoneyField(blank=True, decimal_places=2, default_currency='EUR', max_digits=10, null=True),
        ),
    ]