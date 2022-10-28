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


class Evaluation(models.Model):
    user = models.ForeignKey(User, related_name="evaluations", on_delete=models.CASCADE)

    title = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    issue_description = models.TextField(blank=True, null=True)
    evaluation_type = models.CharField(max_length=128, blank=True, null=True, choices=EvaluationType.choices)
