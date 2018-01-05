# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-05 05:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading', models.FloatField()),
                ('time', models.DateTimeField()),
                ('unit', models.CharField(choices=[(0, 'level'), (1, 'discharge')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('point_type', models.CharField(choices=[(0, 'take_out'), (1, 'rapid'), (2, 'put_in'), (3, 'poi')], max_length=1)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longditude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='River',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level_url', models.URLField()),
                ('river_id', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
                ('minimum', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimum', models.FloatField()),
                ('wikilink', models.URLField()),
                ('river', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.River')),
            ],
        ),
        migrations.CreateModel(
            name='Sectionpoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.Points')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.Section')),
            ],
        ),
        migrations.AddField(
            model_name='levels',
            name='river',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.River'),
        ),
        migrations.AddField(
            model_name='interested',
            name='river',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guide.River'),
        ),
        migrations.AddField(
            model_name='interested',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]