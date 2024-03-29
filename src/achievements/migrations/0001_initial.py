# Generated by Django 4.2.1 on 2023-11-04 17:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Achievement",
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
                ("description", models.CharField(max_length=500)),
                ("phrase", models.CharField(max_length=500)),
                ("name", models.CharField(max_length=50)),
                ("level", models.IntegerField(default=1)),
                ("image", models.URLField(default="https://picsum.photos/200")),
            ],
        ),
        migrations.CreateModel(
            name="AchievementObsession",
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
                (
                    "achievement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="achievements.achievement",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StatisticEntry",
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
                ("name", models.CharField(max_length=50)),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name="Trigger",
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
                ("name", models.CharField(max_length=50)),
                ("value", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                (
                    "achievements",
                    models.ManyToManyField(
                        blank=True, to="achievements.achievementobsession"
                    ),
                ),
                (
                    "statistics",
                    models.ManyToManyField(
                        blank=True, to="achievements.statisticentry"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="achievementobsession",
            name="trigger",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="achievements.statisticentry",
            ),
        ),
        migrations.AddField(
            model_name="achievement",
            name="trigger",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="achievements.trigger"
            ),
        ),
    ]
