# Generated by Django 4.1 on 2022-10-04 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_sensor_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]
