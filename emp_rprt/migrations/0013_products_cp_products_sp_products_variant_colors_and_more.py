# Generated by Django 5.1.2 on 2024-10-28 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_rprt', '0012_alter_progress_work_alter_progressupdated_work_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='cp',
            field=models.IntegerField(default=21),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='sp',
            field=models.IntegerField(default=21),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='variant_colors',
            field=models.CharField(default='color', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='variant_quantity',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]