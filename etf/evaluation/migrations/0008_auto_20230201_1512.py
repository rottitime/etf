# Generated by Django 3.2.16 on 2023-02-01 15:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0007_auto_20230120_1434"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="evaluation",
            name="is_published",
        ),
        migrations.AddField(
            model_name="evaluation",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("DRAFT", "Draft"), ("CIVIL_SERVICE", "Civil Service"), ("PUBLIC", "Public")],
                max_length=256,
            ),
        ),
    ]
