# Generated by Django 3.1.4 on 2020-12-21 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0013_auto_20201221_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='art_image',
            field=models.ImageField(default='DEF', upload_to='images/art'),
            preserve_default=False,
        ),
    ]