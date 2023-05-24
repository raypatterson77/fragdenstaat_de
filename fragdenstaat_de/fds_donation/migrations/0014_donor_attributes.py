# Generated by Django 2.2.4 on 2020-01-21 14:05

import django.contrib.postgres.fields.hstore
from django.contrib.postgres.operations import HStoreExtension
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("fds_donation", "0013_auto_20191220_1329"),
    ]

    operations = [
        HStoreExtension(),
        migrations.AddField(
            model_name="donor",
            name="attributes",
            field=django.contrib.postgres.fields.hstore.HStoreField(
                null=True, blank=True
            ),
        ),
    ]
