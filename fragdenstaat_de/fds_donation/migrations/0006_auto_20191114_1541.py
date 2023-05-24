# Generated by Django 2.2.4 on 2019-11-14 14:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fds_donation", "0005_auto_20191111_1501"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="donationgift",
            options={
                "ordering": ("name",),
                "verbose_name": "donation gift",
                "verbose_name_plural": "donation gifts",
            },
        ),
        migrations.AddField(
            model_name="donation",
            name="purpose",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
