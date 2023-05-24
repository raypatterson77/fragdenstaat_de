# Generated by Django 4.0.7 on 2022-11-25 10:34

from django.db import migrations


def create_plugin_instances(apps, schema_editor):
    CMSPlugin = apps.get_model("cms", "CMSPlugin")
    DropdownBannerCMSPlugin = apps.get_model("fds_cms", "DropdownBannerCMSPlugin")

    plugins = CMSPlugin.objects.filter(plugin_type="DropdownBannerPlugin")
    for plugin in plugins:
        dd_plugin = DropdownBannerCMSPlugin(cmsplugin_ptr_id=plugin.id)
        dd_plugin.__dict__.update(plugin.__dict__)
        dd_plugin.save()


class Migration(migrations.Migration):
    dependencies = [
        ("fds_cms", "0054_dropdownbannercmsplugin"),
    ]

    operations = [migrations.RunPython(create_plugin_instances)]
