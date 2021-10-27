# Generated by Django 2.2.4 on 2019-11-11 14:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("fds_donation", "0004_auto_20191021_1610"),
    ]

    operations = [
        migrations.AddField(
            model_name="donation",
            name="email_sent",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="donor",
            name="active",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="donor",
            name="uuid",
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name="donor",
            name="note",
            field=models.TextField(blank=True),
        ),
    ]
