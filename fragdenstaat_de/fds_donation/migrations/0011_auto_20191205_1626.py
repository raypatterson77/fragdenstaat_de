# Generated by Django 2.2.4 on 2019-12-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fds_donation", "0010_auto_20191205_1610"),
    ]

    operations = [
        migrations.AddField(
            model_name="donation",
            name="receipt_given",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="donation",
            name="recurring",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="donor",
            name="invalid",
            field=models.BooleanField(default=False),
        ),
    ]
