# Generated by Django 3.0.3 on 2020-02-15 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('booking', '0002_auto_20200215_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='user_id',
        ),
        migrations.AddField(
            model_name='coupon',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]