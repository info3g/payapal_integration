# Generated by Django 3.0.3 on 2020-02-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200220_2034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('alt', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(default='index.jpg', upload_to='')),
            ],
        ),
    ]