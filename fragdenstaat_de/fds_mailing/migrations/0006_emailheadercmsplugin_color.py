# Generated by Django 2.2.4 on 2019-11-05 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fds_mailing', '0005_auto_20191105_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailheadercmsplugin',
            name='color',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
