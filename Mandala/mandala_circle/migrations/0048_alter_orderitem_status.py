# Generated by Django 3.2.6 on 2021-09-20 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandala_circle', '0047_auto_20210921_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
