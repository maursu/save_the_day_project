# Generated by Django 4.1.7 on 2023-03-22 10:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("slug", models.SlugField(blank=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("username", models.CharField(max_length=50, unique=True)),
                ("first_name", models.CharField(blank=True, max_length=50)),
                ("last_name", models.CharField(blank=True, max_length=50)),
                ("user_photo", models.ImageField(blank=True, upload_to="account/")),
                ("date_joined", models.DateTimeField(auto_now_add=True)),
                ("twitter_url", models.URLField(blank=True, max_length=255)),
                ("facebook_url", models.URLField(blank=True, max_length=255)),
                ("telegram_url", models.URLField(blank=True, max_length=255)),
                ("about_user", models.CharField(blank=True, max_length=255)),
                ("phone_number", models.CharField(max_length=20)),
                ("is_active", models.BooleanField(default=False)),
                ("is_staff", models.BooleanField(default=False)),
                ("user_type", models.CharField(blank=True, max_length=30)),
                ("verified_account", models.BooleanField(default=False)),
                ("activation_code", models.CharField(max_length=10, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
        ),
    ]
