from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager

from . import choices


class User(BaseUser):
    objects = BaseUserManager()
    username = None

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)


class EvaluationType(choices.Choices):
    UNKNOWN = "Unknown"


class OutcomeType(choices.Choices):
    PRIMARY = "Primary"
    SECONDARY = "Secondary"


class OutcomeMeasure(choices.Choices):
    DIRECT = "Direct"
    SURROGATE = "Surrogate"


class Evaluation(models.Model):
    user = models.ForeignKey(User, related_name="evaluations", on_delete=models.CASCADE)

    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    issue_description = models.TextField(blank=True, null=True)
    evaluation_type = models.CharField(max_length=128, blank=True, null=True, choices=EvaluationType.choices)


class Intervention(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    brief_description = models.TextField(blank=True, null=True)
    rationale = models.TextField(blank=True, null=True)
    materials_used = models.TextField(blank=True, null=True)
    procedures = models.TextField(blank=True, null=True)
    modes_of_delivery = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    frequency_of_delivery = models.TextField(blank=True, null=True)
    tailoring = models.TextField(blank=True, null=True)
    fidelity = models.TextField(blank=True, null=True)
    resource_requirements = models.TextField(blank=True, null=True)
    # TODO - add date


class OutcomeMeasure(models.Model):
    evaluation = models.ForeignKey(Evaluation, related_name="outcome_measures", on_delete=models.CASCADE)
    name = models.CharField(max_length=256, blank=True, null=True)
    primary_or_secondary = models.CharField(max_length=10, blank=True, null=True, choices=OutcomeType.choices)
    direct_or_surrogate = models.CharField(max_length=10, blank=True, null=True, choices=OutcomeMeasure.choices)
    description = models.TextField(blank=True, null=True)
    collection_process = models.TextField(blank=True, null=True)
    timepoint = models.TextField(blank=True, null=True)
    minimum_difference = models.TextField(blank=True, null=True)
    relevance = models.TextField(blank=True, null=True)
