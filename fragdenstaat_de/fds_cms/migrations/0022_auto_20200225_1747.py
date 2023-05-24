# Generated by Django 2.2.4 on 2020-02-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fds_cms", "0021_sharelinkscmsplugin"),
    ]

    operations = [
        migrations.AddField(
            model_name="designcontainercmsplugin",
            name="container",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="designcontainercmsplugin",
            name="background",
            field=models.CharField(
                blank=True,
                choices=[
                    ("primary", "Primary"),
                    ("secondary", "Secondary"),
                    ("info", "Info"),
                    ("light", "Light"),
                    ("dark", "Dark"),
                    ("success", "Success"),
                    ("warning", "Warning"),
                    ("danger", "Danger"),
                    ("purple", "Purple"),
                    ("pink", "Pink"),
                    ("yellow", "Yellow"),
                    ("cyan", "Cyan"),
                    ("gray", "Gray"),
                    ("gray-dark", "Gray Dark"),
                    ("white", "White"),
                    ("gray-100", "Gray 100"),
                    ("gray-200", "Gray 200"),
                    ("gray-300", "Gray 300"),
                    ("gray-400", "Gray 400"),
                    ("gray-500", "Gray 500"),
                    ("gray-600", "Gray 600"),
                    ("gray-700", "Gray 700"),
                    ("gray-800", "Gray 800"),
                    ("gray-900", "Gray 900"),
                    ("blue-100", "Blue 100"),
                    ("blue-200", "Blue 200"),
                    ("blue-300", "Blue 300"),
                    ("blue-400", "Blue 400"),
                    ("blue-500", "Blue 500"),
                    ("blue-600", "Blue 600"),
                    ("blue-700", "Blue 700"),
                    ("blue-800", "Blue 800"),
                ],
                default="",
                max_length=50,
                verbose_name="Background",
            ),
        ),
    ]
