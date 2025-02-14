# Generated by Django 5.0.6 on 2024-05-31 15:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("healthapp", "0007_delete_profile"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="myorders",
            name="qty",
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name="Order",
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
                ("orderid", models.IntegerField()),
                ("qty", models.IntegerField(default=1)),
                ("amount", models.FloatField()),
                (
                    "pid",
                    models.ForeignKey(
                        db_column="pid",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="healthapp.meds",
                    ),
                ),
                (
                    "uid",
                    models.ForeignKey(
                        db_column="uid",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
