# Generated by Django 3.0.3 on 2020-02-19 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_article_summary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='summary',
        ),
    ]
