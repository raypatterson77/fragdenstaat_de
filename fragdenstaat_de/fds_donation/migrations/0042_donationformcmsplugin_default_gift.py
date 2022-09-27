# Generated by Django 4.0.7 on 2022-09-27 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fds_donation', '0041_alter_donationgift_options_donationgift_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationformcmsplugin',
            name='default_gift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='donation_plugin_with_default', to='fds_donation.donationgift'),
        ),
    ]
