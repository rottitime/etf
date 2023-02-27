# Generated by Django 3.2.18 on 2023-02-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0008_alter_evaluation_economic_eval_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluation',
            name='impact_eval_interpretation',
            field=models.CharField(blank=True, choices=[('COST_MINIMISATION', 'Cost minimisation'), ('COST_EFFECTIVENESS_ANALYSIS', 'Cost-effectiveness analysis'), ('COST_BENEFIT_ANALYSIS', 'Cost-benefit analysis'), ('COST_UTILITY_ANALYSIS', 'Cost-utility analysis')], max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='othermeasure',
            name='measure_type',
            field=models.CharField(blank=True, choices=[('CONTINUOUS', 'Continuous'), ('DISCRETE', 'Discrete'), ('BINARY', 'Binary'), ('ORDINAL', 'Ordinal'), ('NOMINAL', 'Nominal'), ('OTHER', 'Other')], max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='outcomemeasure',
            name='measure_type',
            field=models.CharField(blank=True, choices=[('CONTINUOUS', 'Continuous'), ('DISCRETE', 'Discrete'), ('BINARY', 'Binary'), ('ORDINAL', 'Ordinal'), ('NOMINAL', 'Nominal'), ('OTHER', 'Other')], max_length=256, null=True),
        ),
    ]
