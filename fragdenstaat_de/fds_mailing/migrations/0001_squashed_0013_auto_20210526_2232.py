# Generated by Django 3.1.8 on 2021-06-21 08:50

import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import filer.fields.image
import fragdenstaat_de.fds_mailing.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        ("fds_newsletter", "0001_squashed_0010_auto_20210621_1022"),
        ("filer", "__first__"),
        ("fds_donation", "0017_auto_20200131_1050"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailSectionCMSPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="fds_mailing_emailsectioncmsplugin",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255)),
            ],
            options={
                "abstract": False,
            },
            bases=(
                fragdenstaat_de.fds_mailing.models.VariableTemplateMixin,
                "cms.cmsplugin",
            ),
        ),
        migrations.CreateModel(
            name="EmailHeaderCMSPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="fds_mailing_emailheadercmsplugin",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                ("label", models.CharField(max_length=255)),
                (
                    "image",
                    filer.fields.image.FilerImageField(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.FILER_IMAGE_MODEL,
                        verbose_name="image",
                    ),
                ),
                ("color", models.CharField(blank=True, max_length=10)),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
        migrations.CreateModel(
            name="EmailStoryCMSPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="fds_mailing_emailstorycmsplugin",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                ("heading", models.CharField(blank=True, max_length=255)),
                ("url", models.URLField(blank=True, max_length=255)),
                ("label", models.CharField(blank=True, max_length=255)),
            ],
            options={
                "abstract": False,
            },
            bases=(
                fragdenstaat_de.fds_mailing.models.VariableTemplateMixin,
                "cms.cmsplugin",
            ),
        ),
        migrations.CreateModel(
            name="EmailTemplate",
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
                ("name", models.CharField(max_length=255)),
                ("created", models.DateTimeField(default=django.utils.timezone.now)),
                ("updated", models.DateTimeField(default=django.utils.timezone.now)),
                ("category", models.CharField(blank=True, max_length=30)),
                ("subject", models.CharField(blank=True, max_length=255)),
                (
                    "template",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("", "Default template"),
                            ("newsletter", "Newsletter template"),
                            ("formal", "Formal email template"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "email_body",
                    cms.models.fields.PlaceholderField(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        slotname="email_body",
                        to="cms.placeholder",
                    ),
                ),
                ("active", models.BooleanField(default=False)),
                ("mail_intent", models.CharField(blank=True, max_length=255)),
                ("text", models.TextField(blank=True)),
            ],
            options={
                "verbose_name": "email template",
                "verbose_name_plural": "email templates",
                "ordering": ("-created",),
            },
        ),
        migrations.CreateModel(
            name="Mailing",
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
                ("name", models.CharField(max_length=255)),
                ("sender_name", models.CharField(max_length=255)),
                (
                    "sender_email",
                    models.EmailField(default="info@fragdenstaat.de", max_length=255),
                ),
                (
                    "created",
                    models.DateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "publish",
                    models.BooleanField(
                        db_index=True,
                        default=True,
                        help_text="Publish in archive.",
                        verbose_name="publish",
                    ),
                ),
                ("ready", models.BooleanField(default=False, verbose_name="ready")),
                (
                    "submitted",
                    models.BooleanField(
                        default=False, editable=False, verbose_name="submitted"
                    ),
                ),
                (
                    "sending_date",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="sending date"
                    ),
                ),
                (
                    "sent_date",
                    models.DateTimeField(
                        blank=True, editable=False, null=True, verbose_name="sent date"
                    ),
                ),
                (
                    "sent",
                    models.BooleanField(
                        default=False, editable=False, verbose_name="sent"
                    ),
                ),
                (
                    "sending",
                    models.BooleanField(
                        default=False, editable=False, verbose_name="sending"
                    ),
                ),
                (
                    "email_template",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="fds_mailing.emailtemplate",
                    ),
                ),
                (
                    "creator_user",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="mailings_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender_user",
                    models.ForeignKey(
                        blank=True,
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="mailings_sent",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "newsletter",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="fds_newsletter.newsletter",
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
                "verbose_name": "mailing",
                "verbose_name_plural": "mailings",
            },
        ),
        migrations.CreateModel(
            name="EmailActionCMSPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="fds_mailing_emailactioncmsplugin",
                        serialize=False,
                        to="cms.cmsplugin",
                    ),
                ),
                ("heading", models.CharField(blank=True, max_length=255)),
                ("action_url", models.CharField(blank=True, max_length=255)),
                ("action_label", models.CharField(blank=True, max_length=255)),
            ],
            options={
                "abstract": False,
            },
            bases=("cms.cmsplugin",),
        ),
        migrations.CreateModel(
            name="MailingMessage",
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
                ("name", models.CharField(blank=True, max_length=255)),
                ("email", models.EmailField(max_length=255)),
                ("sent", models.DateTimeField(blank=True, null=True)),
                ("bounced", models.BooleanField(default=False)),
                ("message", models.TextField(blank=True)),
                (
                    "donor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="fds_donation.donor",
                    ),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="recipients",
                        to="fds_mailing.mailing",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "subscriber",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="fds_newsletter.subscriber",
                    ),
                ),
            ],
            options={
                "ordering": ("-sent",),
                "verbose_name": "mailing message",
                "verbose_name_plural": "mailing messages",
            },
        ),
    ]
