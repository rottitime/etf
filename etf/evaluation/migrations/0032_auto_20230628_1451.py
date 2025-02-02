# Generated by Django 3.2.18 on 2023-06-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0031_remove_evaluation_short_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="evaluation",
            name="impact_findings",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="impact_summary_findings",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="process_findings",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="evaluation",
            name="process_summary_findings",
            field=models.TextField(blank=True, null=True),
        ),
    ]
