# Generated by Django 3.2.11 on 2022-01-17 14:41

from django.db import migrations


def migrate_extraclasses(apps, schema_editor):
    # cardinner was left out in 0036 by mistake
    Model = apps.get_model("fds_cms", "cardinnercmsplugin")

    items = Model.objects.filter(extra_classes__isnull=False)
    for item in items:
        item.attributes["class"] = item.extra_classes
        item.save()


class Migration(migrations.Migration):

    dependencies = [
        ("fds_cms", "0036_extraclasses_to_attributes"),
    ]

    operations = [
        migrations.RunPython(migrate_extraclasses, atomic=False),
        migrations.RemoveField(
            model_name="cardcmsplugin",
            name="extra_classes",
        ),
        migrations.RemoveField(
            model_name="cardheadercmsplugin",
            name="extra_classes",
        ),
        migrations.RemoveField(
            model_name="cardiconcmsplugin",
            name="extra_classes",
        ),
        migrations.RemoveField(
            model_name="cardimagecmsplugin",
            name="extra_classes",
        ),
        migrations.RemoveField(
            model_name="cardinnercmsplugin",
            name="extra_classes",
        ),
    ]
