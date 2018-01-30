# Generated by Django 2.0.1 on 2018-01-24 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rivers', '0013_auto_20180124_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='unit',
            field=models.IntegerField(choices=[(0, 'level'), (1, 'discharge')], max_length=1),
        ),
        migrations.AlterField(
            model_name='point',
            name='point_type',
            field=models.IntegerField(choices=[(0, 'Take out'), (1, 'Put in'), (2, 'Rapid'), (3, 'Point of interest')], max_length=1),
        ),
    ]