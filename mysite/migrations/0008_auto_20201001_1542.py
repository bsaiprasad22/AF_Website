# Generated by Django 2.2.13 on 2020-10-01 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_udaan_event_udaan_image_udaan_static'),
    ]

    operations = [
        migrations.AlterField(
            model_name='udaan_static',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
