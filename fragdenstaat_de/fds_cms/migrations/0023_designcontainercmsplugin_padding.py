# Generated by Django 2.2.4 on 2020-03-13 14:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fds_cms", "0022_auto_20200225_1747"),
    ]

    operations = [
        migrations.AddField(
            model_name="designcontainercmsplugin",
            name="padding",
            field=models.BooleanField(default=True),
        ),
    ]
