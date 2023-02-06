# Generated by Django 3.2.16 on 2023-02-06 13:54

from django.db import migrations, models

import etf.evaluation.models


class Migration(migrations.Migration):
    dependencies = [
        ("evaluation", "0009_merge_0008_auto_20230201_1512_0008_auto_20230203_0824"),
    ]

    operations = [
        migrations.AlterField(
            model_name="evaluation",
            name="status",
            field=models.CharField(
                choices=[("DRAFT", "Draft"), ("CIVIL_SERVICE", "Civil Service"), ("PUBLIC", "Public")],
                default=etf.evaluation.models.EvaluationStatus["DRAFT"],
                max_length=256,
            ),
        ),
    ]
