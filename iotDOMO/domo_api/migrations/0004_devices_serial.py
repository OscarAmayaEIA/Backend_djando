# Generated by Django 4.2.10 on 2024-03-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("domo_api", "0003_devices_dots"),
    ]

    operations = [
        migrations.AddField(
            model_name="devices",
            name="Serial",
            field=models.CharField(default="000", max_length=255),
            preserve_default=False,
        ),
    ]
