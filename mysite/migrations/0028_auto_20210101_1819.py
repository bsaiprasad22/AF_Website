# Generated by Django 3.1.4 on 2021-01-01 18:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0027_auto_20210101_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 1, 18, 19, 21, 205634, tzinfo=utc)),
        ),
    ]
