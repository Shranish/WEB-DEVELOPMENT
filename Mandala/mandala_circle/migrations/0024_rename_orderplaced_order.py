# Generated by Django 3.2.6 on 2021-09-14 17:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mandala_circle', '0023_orderplaced'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderPlaced',
            new_name='Order',
        ),
    ]
