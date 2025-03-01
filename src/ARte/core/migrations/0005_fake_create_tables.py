# Generated by Django 2.2.24 on 2021-06-20 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_rename_model_tables"),
        ("core", "0004_delete_artwork2"),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name="Artwork",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        ("title", models.CharField(max_length=50)),
                        ("description", models.TextField(blank=True, max_length=500)),
                        ("created_at", models.DateTimeField(auto_now=True)),
                    ],
                ),
                migrations.CreateModel(
                    name="Object",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        ("source", models.FileField(upload_to="objects/")),
                        ("uploaded_at", models.DateTimeField(auto_now=True)),
                        ("author", models.CharField(max_length=60)),
                        ("title", models.CharField(default="", max_length=60)),
                        ("scale", models.CharField(default="1 1", max_length=50)),
                        ("position", models.CharField(default="0 0 0", max_length=50)),
                        (
                            "rotation",
                            models.CharField(default="270 0 0", max_length=50),
                        ),
                        (
                            "owner",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                to="users.Profile",
                            ),
                        ),
                    ],
                ),
                migrations.CreateModel(
                    name="Marker",
                    fields=[
                        (
                            "id",
                            models.AutoField(
                                auto_created=True,
                                primary_key=True,
                                serialize=False,
                                verbose_name="ID",
                            ),
                        ),
                        ("source", models.ImageField(upload_to="markers/")),
                        ("uploaded_at", models.DateTimeField(auto_now=True)),
                        ("author", models.CharField(max_length=60)),
                        ("title", models.CharField(default="", max_length=60)),
                        ("patt", models.FileField(upload_to="patts/")),
                        (
                            "owner",
                            models.ForeignKey(
                                on_delete=django.db.models.deletion.DO_NOTHING,
                                to="users.Profile",
                            ),
                        ),
                    ],
                ),
                migrations.AlterField(
                    model_name="exhibit",
                    name="artworks",
                    field=models.ManyToManyField(
                        related_name="exhibits", to="core.Artwork"
                    ),
                ),
                migrations.AddField(
                    model_name="artwork",
                    name="augmented",
                    field=models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="core.Object"
                    ),
                ),
                migrations.AddField(
                    model_name="artwork",
                    name="author",
                    field=models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="users.Profile",
                    ),
                ),
                migrations.AddField(
                    model_name="artwork",
                    name="marker",
                    field=models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="core.Marker"
                    ),
                ),
            ],
            database_operations=[],
        ),
    ]
