# Generated by Django 3.2.9 on 2022-07-16 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cal", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="description",
        ),
        migrations.RemoveField(
            model_name="event",
            name="end_time",
        ),
        migrations.RemoveField(
            model_name="event",
            name="start_time",
        ),
        migrations.RemoveField(
            model_name="event",
            name="title",
        ),
        migrations.AddField(
            model_name="event",
            name="day",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="event",
            name="hour",
            field=models.IntegerField(default="1"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="event",
            name="month",
            field=models.IntegerField(default="1"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="event",
            name="user",
            field=models.ForeignKey(
                default="1", on_delete=django.db.models.deletion.CASCADE, to="auth.user"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="event",
            name="year",
            field=models.IntegerField(default="2022"),
            preserve_default=False,
        ),
    ]
