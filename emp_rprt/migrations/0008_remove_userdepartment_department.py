# Generated by Django 5.1.2 on 2024-10-24 08:53

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("emp_rprt", "0007_remove_progress_department"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userdepartment",
            name="department",
        ),
    ]
