# Generated by Django 5.1.2 on 2024-10-24 07:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("emp_rprt", "0004_rename_empposition_position"),
    ]

    operations = [
        migrations.CreateModel(
            name="WorkflowStage",
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
                ("title", models.CharField(max_length=255)),
                (
                    "next_stages",
                    models.ManyToManyField(
                        blank=True,
                        related_name="previous_stages",
                        to="emp_rprt.workflowstage",
                    ),
                ),
            ],
        ),
    ]
