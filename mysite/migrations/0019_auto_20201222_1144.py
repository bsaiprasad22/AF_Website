# Generated by Django 3.1.4 on 2020-12-22 11:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0018_auto_20201222_1040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 22, 11, 44, 56, 934938, tzinfo=utc)),
        ),
    ]
