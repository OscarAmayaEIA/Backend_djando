# Generated by Django 4.2.10 on 2024-03-01 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("domo_api", "0002_rename_user_id_locations_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Devices",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("unit", models.CharField(max_length=255)),
                ("name_devices", models.CharField(max_length=255)),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="domo_api.locations",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Dots",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.FloatField()),
                ("date_time", models.DateTimeField(auto_now_add=True)),
                (
                    "device",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="domo_api.devices",
                    ),
                ),
            ],
        ),
    ]
