# Generated by Django 3.1.4 on 2020-12-23 05:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0020_auto_20201222_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AddField(
            model_name='member',
            name='active',
            field=models.BooleanField(default=True, verbose_name='member status'),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 23, 5, 5, 42, 311754, tzinfo=utc)),
        ),
    ]
