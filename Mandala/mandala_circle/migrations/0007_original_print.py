# Generated by Django 3.2.6 on 2021-09-10 08:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandala_circle', '0006_auto_20210909_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Original',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=500, null=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('product_price', models.FloatField()),
                ('product_description', models.TextField(max_length=1000, null=True)),
                ('product_image', models.ImageField(upload_to='static/uploads')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Print',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('print_name', models.CharField(max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('print_price', models.FloatField()),
                ('print_description', models.TextField(max_length=100, null=True)),
                ('print_image', models.FileField(upload_to='static/uploads')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
