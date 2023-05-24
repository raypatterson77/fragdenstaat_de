# Generated by Django 2.1.4 on 2018-12-18 14:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fds_blog", "0003_auto_20181217_1233"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="language",
            field=models.CharField(
                choices=[("de", "German"), ("en", "English")], max_length=5, null=True
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="user",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="authorship",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="latestarticlesplugin",
            name="article_language",
            field=models.CharField(
                blank=True,
                choices=[("de", "German"), ("en", "English")],
                default="de",
                max_length=5,
                verbose_name="language",
            ),
        ),
    ]
