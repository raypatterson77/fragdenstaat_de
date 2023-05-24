# Generated by Django 2.1.7 on 2019-04-01 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("foirequest", "0039_foirequest_team"),
        ("fds_cms", "0010_fdspageextension"),
    ]

    operations = [
        migrations.CreateModel(
            name="OneClickFoiRequestCMSPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="fds_cms_oneclickfoirequestcmsplugin",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                (
                    "template",
                    models.CharField(
                        blank=True,
                        choices=[("", "Default template")],
                        default="",
                        max_length=50,
                        verbose_name="Template",
                    ),
                ),
                (
                    "foirequest",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="foirequest.FoiRequest",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
    ]
