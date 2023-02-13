# Generated by Django 3.2.16 on 2023-02-13 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("evaluation", "0011_documents_processesandstandards"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventDate",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("EVALUATION_START", "Evaluation start"),
                            ("EVALUATION_END", "Evaluation end"),
                            ("FIRST_PARTICIPANT_RECRUITED", "First participant recruited"),
                            ("LAST_PARTICIPANT_RECRUITED", "Last participant recruited"),
                            ("INTERVENTION_START_DATE", "Intervention start date"),
                            ("INTERVENTION_END_DATE", "Intervention end date"),
                            ("INTERIM_DATA_EXTRACTION_DATE", "Interim data extraction date"),
                            ("INTERIM_DATA_ANALYSIS_START", "Interim data analysis start"),
                            ("INTERIM_DATA_ANALYSIS_END", "Interim data analysis end"),
                            ("PUBLICATION_INTERIM_RESULTS", "Publication of interim results"),
                            ("FINAL_DATA_EXTRACTION_DATE", "Final data extraction date"),
                            ("FINAL_DATA_ANALYSIS_START", "Final data analysis start"),
                            ("FINAL_DATA_ANALYSIS_END", "Final data analysis end"),
                            ("PUBLICATION_FINAL_RESULTS", "Publication of final results"),
                            ("OTHER", "Other"),
                        ],
                        max_length=256,
                        null=True,
                    ),
                ),
                ("date", models.DateField(blank=True, null=True)),
                ("type", models.CharField(blank=True, max_length=10, null=True)),
                ("reasons_for_change", models.TextField(blank=True, null=True)),
                (
                    "evaluation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="event_date",
                        to="evaluation.evaluation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProcessStandard",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=256)),
                (
                    "conformity",
                    models.CharField(
                        blank=True,
                        choices=[("FULL", "Full"), ("PARTIAL", "Partial"), ("NO", "No")],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "evaluation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="process_standard",
                        to="evaluation.evaluation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RenameModel(
            old_name="Documents",
            new_name="Document",
        ),
        migrations.DeleteModel(
            name="ProcessesAndStandards",
        ),
    ]
