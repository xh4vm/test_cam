# Generated by Django 4.2.5 on 2023-09-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=255, unique=True)),
            ],
            options={
                "db_table": "user",
            },
        ),
        migrations.CreateModel(
            name="UserSession",
            fields=[
                (
                    "session_key",
                    models.CharField(
                        max_length=40,
                        primary_key=True,
                        serialize=False,
                        verbose_name="session key",
                    ),
                ),
                ("session_data", models.TextField(verbose_name="session data")),
                (
                    "expire_date",
                    models.DateTimeField(db_index=True, verbose_name="expire date"),
                ),
                ("user_id", models.IntegerField(db_index=True, null=True)),
            ],
            options={
                "db_table": "user_session",
            },
        ),
    ]
