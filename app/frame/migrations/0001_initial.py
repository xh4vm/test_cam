# Generated by Django 4.2.5 on 2023-09-13 20:13

from django.db import migrations, models
import frame.validators


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Frame",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.AutoField(
                        primary_key=True,
                        serialize=False,
                        validators=[frame.validators.frame_id_validator],
                    ),
                ),
                (
                    "cam_id",
                    models.IntegerField(validators=[frame.validators.cam_id_validator]),
                ),
                (
                    "VideoColor",
                    models.JSONField(
                        validators=[frame.validators.video_color_schema_validator]
                    ),
                ),
                ("TimeSection", models.DateTimeField()),
                (
                    "ChannelNo",
                    models.IntegerField(
                        validators=[frame.validators.channel_validator]
                    ),
                ),
                (
                    "ConfigNo",
                    models.IntegerField(validators=[frame.validators.config_validator]),
                ),
            ],
            options={
                "db_table": "frame",
            },
        ),
        migrations.CreateModel(
            name="UserFrame",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("user_id", models.IntegerField()),
                ("frame_id", models.IntegerField()),
            ],
            options={
                "db_table": "user_frame",
            },
        ),
    ]
