# Generated by Django 3.2.6 on 2021-09-20 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mandala_circle', '0052_alter_orderitem_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered')], default='Pending', max_length=50),
        ),
    ]
