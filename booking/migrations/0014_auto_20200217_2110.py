# Generated by Django 3.0.3 on 2020-02-17 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_auto_20200217_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='booking_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='customer_id',
            field=models.IntegerField(),
        ),
    ]