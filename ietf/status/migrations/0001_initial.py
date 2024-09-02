# Generated by Django 4.2.13 on 2024-07-21 22:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("person", "0002_alter_historicalperson_ascii_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Status",
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
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
                ("slug", models.SlugField(unique=True)),
                (
                    "title",
                    models.CharField(
                        help_text="Your site status notification title.",
                        max_length=255,
                        verbose_name="Status title",
                    ),
                ),
                (
                    "body",
                    models.CharField(
                        help_text="Your site status notification body.",
                        max_length=255,
                        verbose_name="Status body",
                    ),
                ),
                (
                    "active",
                    models.BooleanField(
                        default=True,
                        help_text="Only active messages will be shown.",
                        verbose_name="Active?",
                    ),
                ),
                (
                    "page",
                    models.TextField(
                        blank=True,
                        help_text="More detail shown after people click 'Read more'. If empty no 'read more' will be shown",
                        null=True,
                        verbose_name="More detail (markdown)",
                    ),
                ),
                (
                    "by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="person.person"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "statuses",
            },
        ),
    ]