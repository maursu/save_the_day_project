# Generated by Django 4.1.7 on 2023-03-22 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("charity_programs", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Reports",
            fields=[
                ("title", models.CharField(max_length=50)),
                ("body", models.TextField(blank=True)),
                ("posted_at", models.DateTimeField(auto_now_add=True)),
                (
                    "slug",
                    models.SlugField(blank=True, primary_key=True, serialize=False),
                ),
                (
                    "program",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="report",
                        to="charity_programs.program",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Reports",
            },
        ),
        migrations.CreateModel(
            name="ReportImage",
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
                ("image", models.ImageField(blank=True, upload_to="reports_photo/")),
                (
                    "report",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reports.reports",
                    ),
                ),
            ],
        ),
    ]
