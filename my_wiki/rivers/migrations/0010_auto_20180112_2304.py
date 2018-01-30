# Generated by Django 2.0.1 on 2018-01-12 23:04

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('rivers', '0009_auto_20180112_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='markdown',
        ),
        migrations.AddField(
            model_name='section',
            name='description',
            field=markdownx.models.MarkdownxField(default=''),
        ),
    ]