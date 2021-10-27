# Generated by Django 2.2.4 on 2019-12-05 15:10

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ("fds_donation", "0009_auto_20191204_1342"),
    ]

    operations = [
        migrations.CreateModel(
            name="DonorTag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=100, unique=True, verbose_name="Name"),
                ),
                (
                    "slug",
                    models.SlugField(max_length=100, unique=True, verbose_name="Slug"),
                ),
            ],
            options={
                "verbose_name": "Donor Tag",
                "verbose_name_plural": "Donor Tags",
            },
        ),
        migrations.AlterField(
            model_name="donor",
            name="salutation",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Hallo"),
                    ("formal_f", "Sehr geehrte Frau"),
                    ("formal_m", "Sehr geehrter Herr"),
                    ("informal_f", "Liebe"),
                    ("informal_m", "Lieber"),
                ],
                max_length=25,
            ),
        ),
        migrations.CreateModel(
            name="TaggedDonor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "content_object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="fds_donation.Donor",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="donors",
                        to="fds_donation.DonorTag",
                    ),
                ),
            ],
            options={
                "verbose_name": "Tagged Donor",
                "verbose_name_plural": "Tagged Donors",
            },
        ),
        migrations.AddField(
            model_name="donor",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="fds_donation.TaggedDonor",
                to="fds_donation.DonorTag",
                verbose_name="Tags",
            ),
        ),
    ]
