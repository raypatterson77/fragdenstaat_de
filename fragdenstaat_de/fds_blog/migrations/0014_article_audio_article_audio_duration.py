# Generated by Django 4.2.1 on 2023-06-21 12:48

import django.db.models.deletion
from django.db import migrations, models

import filer.fields.file


class Migration(migrations.Migration):
    dependencies = [
        ("filer", "0015_alter_file_owner_alter_file_polymorphic_ctype_and_more"),
        ("fds_blog", "0013_alter_article_related_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="audio",
            field=filer.fields.file.FilerFileField(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="audio_articles",
                to="filer.file",
                verbose_name="audio file",
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="audio_duration",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="duration in seconds"
            ),
        ),
    ]
