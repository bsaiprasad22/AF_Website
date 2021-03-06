# Generated by Django 3.1.4 on 2020-12-29 15:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0023_auto_20201223_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 29, 15, 48, 54, 311049, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='post',
            field=models.CharField(blank=True, help_text='Insert past post names also. ex, <batch> Convener for a past batch convener', max_length=300),
        ),
    ]
