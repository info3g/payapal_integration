# Generated by Django 3.0.3 on 2020-02-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_customer_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='customer',
            name='price',
            field=models.FloatField(),
        ),
    ]