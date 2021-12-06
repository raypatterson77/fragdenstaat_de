# Generated by Django 3.2.8 on 2021-12-06 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('fds_cms', '0033_auto_20211014_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardCMSPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='fds_cms_cardcmsplugin', serialize=False, to='cms.cmsplugin')),
                ('border', models.CharField(choices=[('blue', 'Blue'), ('gray', 'Gray'), ('yellow', 'Yellow')], default='gray', max_length=50, verbose_name='Border')),
                ('shadow', models.CharField(choices=[('no', 'No'), ('auto', 'Auto'), ('always', 'Always')], default='auto', max_length=10, verbose_name='Shadow')),
                ('spacing', models.CharField(choices=[('sm', 'Small'), ('lg', 'Large')], default='small', max_length=3)),
                ('extra_classes', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CardHeaderCMSPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='fds_cms_cardheadercmsplugin', serialize=False, to='cms.cmsplugin')),
                ('title', models.TextField(verbose_name='Title')),
                ('icon', models.CharField(blank=True, max_length=50, verbose_name='Icon')),
                ('extra_classes', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CardInnerCMSPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='fds_cms_cardinnercmsplugin', serialize=False, to='cms.cmsplugin')),
                ('background', models.CharField(blank=True, choices=[('', 'None'), ('primary', 'Primary'), ('secondary', 'Secondary'), ('info', 'Info'), ('light', 'Light'), ('dark', 'Dark'), ('success', 'Success'), ('warning', 'Warning'), ('danger', 'Danger'), ('purple', 'Purple'), ('pink', 'Pink'), ('yellow', 'Yellow'), ('cyan', 'Cyan'), ('gray', 'Gray'), ('gray-dark', 'Gray Dark'), ('white', 'White'), ('gray-100', 'Gray 100'), ('gray-200', 'Gray 200'), ('gray-300', 'Gray 300'), ('gray-400', 'Gray 400'), ('gray-500', 'Gray 500'), ('gray-600', 'Gray 600'), ('gray-700', 'Gray 700'), ('gray-800', 'Gray 800'), ('gray-900', 'Gray 900'), ('blue-10', 'Blue 10'), ('blue-20', 'Blue 20'), ('blue-30', 'Blue 30'), ('blue-100', 'Blue 100'), ('blue-200', 'Blue 200'), ('blue-300', 'Blue 300'), ('blue-400', 'Blue 400'), ('blue-500', 'Blue 500'), ('blue-600', 'Blue 600'), ('blue-700', 'Blue 700'), ('blue-800', 'Blue 800'), ('yellow-100', 'Yellow 100'), ('yellow-200', 'Yellow 200'), ('yellow-300', 'Yellow 300')], default='', max_length=50, verbose_name='Background')),
                ('extra_classes', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
