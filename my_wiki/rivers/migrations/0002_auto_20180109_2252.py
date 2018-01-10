# Generated by Django 2.0.1 on 2018-01-09 22:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rivers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('minimum', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='river',
            name='level_url',
        ),
        migrations.RemoveField(
            model_name='river',
            name='minimum',
        ),
        migrations.RemoveField(
            model_name='river',
            name='river_id',
        ),
        migrations.AddField(
            model_name='section',
            name='river',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rivers.River'),
        ),
    ]