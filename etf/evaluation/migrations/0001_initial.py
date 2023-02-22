# Generated by Django 3.2.18 on 2023-02-22 09:31

import uuid

import django.db.models.deletion
import django.utils.timezone
import django_use_email_as_username.models
from django.conf import settings
from django.db import migrations, models

import etf.evaluation.pages


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=150, verbose_name="first name")),
                ("last_name", models.CharField(blank=True, max_length=150, verbose_name="last name")),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                ("date_joined", models.DateTimeField(default=django.utils.timezone.now, verbose_name="date joined")),
                ("email", models.EmailField(max_length=254, unique=True, verbose_name="email address")),
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("verified", models.BooleanField(blank=True, default=False, null=True)),
                ("last_token_sent_at", models.DateTimeField(blank=True, editable=False, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            managers=[
                ("objects", django_use_email_as_username.models.BaseUserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Evaluation",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(blank=True, max_length=256, null=True)),
                ("short_title", models.CharField(blank=True, max_length=64, null=True)),
                ("brief_description", models.TextField(blank=True, null=True)),
                ("topics", models.JSONField(default=list)),
                ("organisations", models.JSONField(default=list)),
                (
                    "status",
                    models.CharField(
                        choices=[("DRAFT", "Draft"), ("CIVIL_SERVICE", "Civil Service"), ("PUBLIC", "Public")],
                        default="DRAFT",
                        max_length=256,
                    ),
                ),
                ("doi", models.CharField(blank=True, max_length=64, null=True)),
                ("page_statuses", models.JSONField(default=etf.evaluation.pages.get_default_page_statuses)),
                ("issue_description", models.TextField(blank=True, null=True)),
                ("those_experiencing_issue", models.TextField(blank=True, null=True)),
                ("why_improvements_matter", models.TextField(blank=True, null=True)),
                ("who_improvements_matter_to", models.TextField(blank=True, null=True)),
                ("current_practice", models.TextField(blank=True, null=True)),
                ("issue_relevance", models.TextField(blank=True, null=True)),
                ("evaluation_type", models.JSONField(default=list)),
                ("studied_population", models.TextField(blank=True, null=True)),
                ("eligibility_criteria", models.TextField(blank=True, null=True)),
                ("sample_size", models.PositiveIntegerField(blank=True, null=True)),
                ("sample_size_units", models.CharField(blank=True, max_length=256, null=True)),
                ("sample_size_details", models.TextField(blank=True, null=True)),
                ("process_for_recruitment", models.TextField(blank=True, null=True)),
                ("recruitment_schedule", models.TextField(blank=True, null=True)),
                ("ethics_committee_approval", models.BooleanField(blank=True, null=True)),
                ("ethics_committee_details", models.TextField(blank=True, null=True)),
                ("ethical_state_given_existing_evidence_base", models.TextField(blank=True, null=True)),
                ("risks_to_participants", models.TextField(blank=True, null=True)),
                ("risks_to_study_team", models.TextField(blank=True, null=True)),
                ("participant_involvement", models.TextField(blank=True, null=True)),
                ("participant_information", models.TextField(blank=True, null=True)),
                ("participant_consent", models.TextField(blank=True, null=True)),
                ("participant_payment", models.TextField(blank=True, null=True)),
                ("confidentiality_and_personal_data", models.TextField(blank=True, null=True)),
                ("breaking_confidentiality", models.TextField(blank=True, null=True)),
                ("other_ethical_information", models.TextField(blank=True, null=True)),
                ("impact_eval_design_name", models.JSONField(default=list)),
                ("impact_eval_design_justification", models.TextField(blank=True, null=True)),
                ("impact_eval_design_description", models.TextField(blank=True, null=True)),
                ("impact_eval_design_features", models.TextField(blank=True, null=True)),
                ("impact_eval_design_equity", models.TextField(blank=True, null=True)),
                ("impact_eval_design_assumptions", models.TextField(blank=True, null=True)),
                ("impact_eval_design_approach_limitations", models.TextField(blank=True, null=True)),
                ("impact_eval_analysis_set", models.TextField(blank=True, null=True)),
                ("impact_eval_effect_measure", models.TextField(blank=True, null=True)),
                ("process_eval_methods", models.CharField(blank=True, max_length=256, null=True)),
                ("process_eval_analysis_description", models.TextField(blank=True, null=True)),
                ("economic_eval_type", models.CharField(blank=True, max_length=256, null=True)),
                ("economic_eval_analysis_description", models.TextField(blank=True, null=True)),
                ("other_eval_design_type", models.TextField(blank=True, null=True)),
                ("other_eval_design_details", models.TextField(blank=True, null=True)),
                ("other_eval_analysis_description", models.TextField(blank=True, null=True)),
                ("impact_eval_comparison", models.TextField(blank=True, null=True)),
                ("impact_eval_outcome", models.TextField(blank=True, null=True)),
                ("economic_eval_summary_findings", models.TextField(blank=True, null=True)),
                ("economic_eval_findings", models.TextField(blank=True, null=True)),
                ("process_eval_summary_findings", models.TextField(blank=True, null=True)),
                ("process_eval_findings", models.TextField(blank=True, null=True)),
                ("other_eval_summary_findings", models.TextField(blank=True, null=True)),
                ("other_eval_findings", models.TextField(blank=True, null=True)),
                ("users", models.ManyToManyField(related_name="evaluations", to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProcessStandard",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
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
                        related_name="process_standards",
                        to="evaluation.evaluation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OutcomeMeasure",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "primary_or_secondary",
                    models.CharField(
                        blank=True,
                        choices=[("PRIMARY", "Primary"), ("SECONDARY", "Secondary")],
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "direct_or_surrogate",
                    models.CharField(
                        blank=True, choices=[("DIRECT", "Direct"), ("SURROGATE", "Surrogate")], max_length=10, null=True
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("collection_process", models.TextField(blank=True, null=True)),
                ("timepoint", models.TextField(blank=True, null=True)),
                ("minimum_difference", models.TextField(blank=True, null=True)),
                ("relevance", models.TextField(blank=True, null=True)),
                (
                    "evaluation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="outcome_measures",
                        to="evaluation.evaluation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OtherMeasure",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("collection_process", models.TextField(blank=True, null=True)),
                (
                    "evaluation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="other_measures",
                        to="evaluation.evaluation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="LinkOtherService",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("name_of_service", models.CharField(blank=True, max_length=256, null=True)),
                ("link_or_identifier", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "evaluation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="link_other_services",
                        to="evaluation.evaluation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Intervention",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=256, null=True)),
                ("brief_description", models.TextField(blank=True, null=True)),
                ("rationale", models.TextField(blank=True, null=True)),
                ("materials_used", models.TextField(blank=True, null=True)),
                ("procedures", models.TextField(blank=True, null=True)),
                ("provider_description", models.TextField(blank=True, null=True)),
                ("modes_of_delivery", models.TextField(blank=True, null=True)),
                ("location", models.TextField(blank=True, null=True)),
                ("frequency_of_delivery", models.TextField(blank=True, null=True)),
                ("tailoring", models.TextField(blank=True, null=True)),
                ("fidelity", models.TextField(blank=True, null=True)),
                ("resource_requirements", models.TextField(blank=True, null=True)),
                ("geographical_information", models.TextField(blank=True, null=True)),
                (
                    "evaluation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="interventions",
                        to="evaluation.evaluation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EventDate",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
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
                        related_name="event_dates",
                        to="evaluation.evaluation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EvaluationType",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("IMPACT", "Impact evaluation"),
                            ("PROCESS", "Process evaluation"),
                            ("ECONOMIC_COST_MINIMISATION", "Economic evaluation: Cost-minimisation analysis"),
                            ("ECONOMIC_COST_EFFECTIVENESS", "Economic evaluation: Cost-effectiveness analysis"),
                            ("ECONOMIC_COST_BENEFIT", "Economic evaluation: Cost-benefit analysis"),
                            ("ECONOMIC_COST_UTILITY", "Economic evaluation: Cost-utility"),
                            ("OTHER", "Other"),
                        ],
                        max_length=256,
                        null=True,
                    ),
                ),
                ("other_description", models.CharField(blank=True, max_length=256, null=True)),
                (
                    "evaluation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="evaluation_types",
                        to="evaluation.evaluation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EvaluationCost",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("item_name", models.TextField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("item_cost", models.FloatField(blank=True, null=True)),
                ("earliest_spend_date", models.DateField(blank=True, null=True)),
                ("latest_spend_date", models.DateField(blank=True, null=True)),
                (
                    "evaluation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="costs", to="evaluation.evaluation"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=256)),
                ("url", models.URLField(blank=True, max_length=512, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "evaluation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="documents",
                        to="evaluation.evaluation",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
