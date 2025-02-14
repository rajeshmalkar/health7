# Generated by Django 5.0.6 on 2024-06-01 07:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("healthapp", "0009_remove_order_pid_remove_myorders_pid_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="product",
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
                ("name", models.CharField(max_length=100, verbose_name="Product Name")),
                ("price", models.FloatField()),
                (
                    "cat",
                    models.IntegerField(
                        choices=[
                            (1, "Frontend"),
                            (2, "Backend"),
                            (3, "Database"),
                            (4, "Devops"),
                            (5, "DSA"),
                        ],
                        max_length=50,
                        verbose_name="Category",
                    ),
                ),
                (
                    "cdetail",
                    models.CharField(max_length=300, verbose_name="Product Detail"),
                ),
                ("cimage", models.ImageField(upload_to="image")),
                ("is_active", models.BooleanField(default=True)),
            ],
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
                    "uid",
                    models.ForeignKey(
                        db_column="uid",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "pid",
                    models.ForeignKey(
                        db_column="pid",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="healthapp.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cart",
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
                ("qty", models.IntegerField(default=1)),
                (
                    "uid",
                    models.ForeignKey(
                        db_column="uid",
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "pid",
                    models.ForeignKey(
                        db_column="pid",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="healthapp.product",
                    ),
                ),
            ],
        ),
    ]
