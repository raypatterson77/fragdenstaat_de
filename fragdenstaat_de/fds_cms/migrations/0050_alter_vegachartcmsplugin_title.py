# Generated by Django 3.2.12 on 2022-07-27 13:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fds_cms", "0049_borderedsectioncmsplugin"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vegachartcmsplugin",
            name="title",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
