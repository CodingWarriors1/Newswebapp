# Generated by Django 3.0.3 on 2020-03-14 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_news_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='act',
            field=models.IntegerField(default=0),
        ),
    ]
