# Generated by Django 3.2.4 on 2021-07-07 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fds_donation", "0033_auto_20210617_1238"),
    ]

    operations = [
        migrations.AlterField(
            model_name="donor",
            name="salutation",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Hallo"),
                    ("formal", "Guten Tag"),
                    ("formal_f", "Sehr geehrte Frau"),
                    ("formal_m", "Sehr geehrter Herr"),
                    ("informal_f", "Liebe"),
                    ("informal_m", "Lieber"),
                    ("informal_n", "Liebes"),
                ],
                max_length=25,
            ),
        ),
    ]
